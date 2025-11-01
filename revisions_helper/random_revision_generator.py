import argparse
import json
import os
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # repo root (LeetCode/)
REVISIONS_FILE = ROOT / "site" / "src" / "data" / "revisions.json"
SOLUTIONS_ROOT = ROOT / "solutions" / "python"

def load_revisions():
    if not REVISIONS_FILE.exists():
        print("Revisions file not found:", REVISIONS_FILE)
        sys.exit(2)
    return json.loads(REVISIONS_FILE.read_text(encoding="utf8"))

def find_revision(revisions, rev_id):
    for r in revisions:
        if str(r.get("id")) == str(rev_id):
            return r
    return None

def solution_path_for(problem_id, language, ext, rev_id):
    return SOLUTIONS_ROOT / str(problem_id) / f"rev_{rev_id}.{ext}"

def pick_next_problem(rev, create_placeholder=False):
    language = rev.get("language", "python")
    ext = rev.get("ext", "py")
    problem_ids = rev.get("problemIds", [])
    remaining = []
    for pid in problem_ids:
        pth = solution_path_for(pid, language, ext, rev["id"])
        if not pth.exists():
            remaining.append((pid, pth))

    if not remaining:
        return None, []

    pid, pth = random.choice(remaining)
    if create_placeholder:
        pth.parent.mkdir(parents=True, exist_ok=True)
        if not pth.exists():
            pth.write_text(f"# Placeholder for revision {rev['id']} on problem {pid}\n", encoding="utf8")
    return pid, remaining

def main():
    ap = argparse.ArgumentParser(description="Select next random problem from a revision (skips completed).")
    ap.add_argument("--rev", "-r", required=False, help="Revision id (from site/src/data/revisions.json).")
    ap.add_argument("--list", action="store_true", help="List revisions and exit.")
    ap.add_argument("--create", action="store_true", help="Create placeholder rev_<id>.py for selected problem.")
    args = ap.parse_args()

    revisions = load_revisions()
    if args.list or not args.rev:
        print("Available revisions (id, title):")
        for r in revisions:
            print(f"  {r.get('id')}: {r.get('title')}")
        if not args.rev:
            return

    rev = find_revision(revisions, args.rev)
    if not rev:
        print(f"Revision {args.rev} not found in {REVISIONS_FILE}")
        sys.exit(3)

    pid, remaining = pick_next_problem(rev, create_placeholder=args.create)
    if pid is None:
        print(f"All problems for revision {rev['id']} are completed.")
        print("Completed count:", len(rev.get("problemIds", [])))
        return

    print(f"Selected problem id: {pid}")
    print("Placeholder path (expected when completed):", solution_path_for(pid, rev.get("language","python"), rev.get("ext","py"), rev["id"]))
    print(f"{len(remaining)-1} remaining after this selection.")
    # Optionally print remaining ids
    # print("Remaining ids:", [p for p,_ in remaining if p != pid])

if __name__ == "__main__":
    main()