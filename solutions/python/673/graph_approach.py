"""
Given a list of numbers `nums`, this snippet counts **all** Longest Increasing
Subsequences (LIS) in `nums` using a graph‑based dynamic‑programming approach.

High‑level algorithm
--------------------
1. **Graph construction** – build a directed acyclic graph (DAG) whose vertices
   are the indices `0 … n‑1`; create an edge `j → i` whenever `j < i` and
   `nums[j] < nums[i]`.  Every path in this DAG corresponds to one strictly
   increasing subsequence.
2. **Topological sort** – process the DAG in topological order so that all
   predecessors of a vertex are handled before the vertex itself.
3. **Dynamic programming** – while iterating in topological order, maintain
   `length[v]` (length of the LIS ending at `v`) and `count[v]` (number of such
   sequences).  Update a child `c` from a parent `p` exactly as one would update
   the LIS relation `… → p → c`.
4. **Aggregate answer** – the overall LIS length is `max(length)`; summing the
   corresponding counts gives the required answer.

Time complexity: **O(n²)** – dominated by the double loop that tries every pair
of indices once.  Space complexity: **O(n²)** in the worst case for the dense
adjacency list, though the dynamic‑programming arrays are only **O(n)**.
"""

from collections import deque
from typing import List

# ------------------------------------------------------------
# 1. Pre‑processing and graph construction
# ------------------------------------------------------------
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        n = len(nums)                           # total number of elements

        # Adjacency list: graph[u] contains all vertices v such that u → v
        graph = {i: [] for i in range(n)}

        for i in range(n):                      # consider every potential *child* index i
            for j in range(i):                  # consider every earlier *parent* index j
                if nums[j] < nums[i]:           # edge only if the value increases
                    graph[j].append(i)          # add directed edge j → i

        print(graph)                            
        # ------------------------------------------------------------
        # 2. Compute indegrees for Kahn’s topological sort
        # ------------------------------------------------------------

        indegree = {i: 0 for i in range(n)}
        for _, children in graph.items():
            for child in children:
                indegree[child] += 1            # child has one more incoming edge

        # ------------------------------------------------------------
        # 3. Kahn’s algorithm to obtain a topological ordering
        # ------------------------------------------------------------

        topsort = []                            # resulting topological order
        queue = deque([v for v, deg in indegree.items() if deg == 0])  # all sources

        while queue:
            node = queue.popleft()
            topsort.append(node)

            for child in graph[node]:
                indegree[child] -= 1            # remove the edge node → child
                if indegree[child] == 0:        # child becomes a new source
                    queue.append(child)


        # ------------------------------------------------------------
        # 4. Dynamic programming over the DAG to count LISs
        # ------------------------------------------------------------

        # Example walk‑through
        # --------------------
        # Let nums = [1, 3, 2, 4]
        #   graph   = {0: [1, 2, 3], 1: [3], 2: [3], 3: []}
        #   topsort = [0, 1, 2, 3]  (one valid order)
        #   Initially length = [1, 1, 1, 1] and count = [1, 1, 1, 1]
        #
        #   • node = 0
        #       → child 1 : new best → length[1] = 2, count[1] = 1
        #       → child 2 : new best → length[2] = 2, count[2] = 1
        #       → child 3 : new best → length[3] = 2, count[3] = 1
        #   • node = 1
        #       → child 3 : new best (3 > 2) → length[3] = 3, count[3] = count[1] = 1
        #   • node = 2
        #       → child 3 : tie (3 == 3) → count[3] += count[2] → count[3] = 2
        #
        #   Final arrays: length = [1, 2, 2, 3], count = [1, 1, 1, 2]
        #   LIS length  = 3 (subsequences [1, 3, 4] and [1, 2, 4])

        length = [1] * n                        # LIS length ending at each vertex
        count  = [1] * n                        # number of such LISs ending at vertex

        for node in topsort:                    # invariant: all parents of `node` done
            for child in graph[node]:           # traverse all edges node → child
                # If going through `node` yields a longer subsequence for `child`...
                if length[node] + 1 > length[child]:
                    length[child] = length[node] + 1
                    count[child]  = count[node]            # reset count: new best path
                # If it ties the current best length for `child`, accumulate counts.
                elif length[node] + 1 == length[child]:
                    count[child] += count[node]


        # ------------------------------------------------------------
        # 5. Compute final answer
        # ------------------------------------------------------------

        lis_len = max(length)                   # global longest length
        ans = sum(c for l, c in zip(length, count) if l == lis_len)
        return ans
"""
Observe that 0,1,2,3,4,5,6... 
is always a valid topological sort for this problem why because edges of form j->i are only added
to the graph if j<i and nums[j] <nums[i]
# ---------------------------------------------------------------------
# Topological ordering & why the plain index order (0, 1, 2, … , n-1)
# is already one for the “edges-when-nums[j] < nums[i]” graph
# ---------------------------------------------------------------------
#
# 1.  What is a *topological order*?
#     --------------------------------
#     • A *directed acyclic graph* (DAG) has no directed cycles.
#     • A *topological ordering* of a DAG is any linear list of vertices
#       in which every edge points **forward**.  Formally, for every edge
#       u → v, vertex *u* appears **before** vertex *v* in the list.
#     • A DAG can have many such orders; at least one always exists.
#
#       Simple ASCII sketch:
#
#           u ──▶ v ──▶ w
#           │
#           └────────▶ x
#
#       One valid topological order here is:   u, v, x, w
#       – u precedes both v and x; v precedes w – so all arrows go left➜right.
#
# 2.  Why the LIS graph is automatically a DAG whose edges honor index order
#     ---------------------------------------------------------------------
#     Our nested loops build edges like this:
#
#         for i in range(n):          # i  = later index   (0-based)
#             for j in range(i):      # j  = earlier index (< i)
#                 if nums[j] < nums[i]:
#                     graph[j].append(i)   # add edge  j → i
#
#     Two facts hold for every stored edge j → i:
#       (a) Index monotonicity : j < i                (inherent in the loops)
#       (b) Value monotonicity : nums[j] < nums[i]    (enforced by the `if`)
#
#     Because the index always *increases* along every edge, you can’t start
#     at some vertex and follow edges “forward” and ever return to yourself.
#     Hence the structure is acyclic – by definition a DAG.
#
# 3.  Why the plain index list 0, 1, 2, … , n-1 is already a topo order
#     -----------------------------------------------------------------
#     Take the natural ordering of vertices by index:
#
#         0, 1, 2, … , n-1
#
#     For ANY edge j → i we inserted, we know j < i, so vertex j appears to
#     the **left** of i in that list.  Consequently **every** edge points
#     forward in this ordering – exactly the requirement for a topological
#     sort.  No Kahn’s algorithm or DFS post-order stack is needed.
#
#     Practical payoff:
#       • You can replace the whole explicit topological-sorting phase with
#           topsort = range(n)          # 0,1,2,…,n-1
#       • The subsequent DP step (propagating length[] and count[]) still
#         works because it only needs *some* valid topo order – and we have
#         one “for free.”
#       • Asymptotic runtime remains O(n²); we just save constant overhead.
#
# ---------------------------------------------------------------------

"""