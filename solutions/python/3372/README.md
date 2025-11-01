Problem Statement

We have two undirected trees with distinct labels:

Tree A contains n nodes labelled 0 … n‑1 and is described by edges1 (length n‑1).

Tree B contains m nodes labelled 0 … m‑1 and is described by edges2 (length m‑1).

For a non–negative integer k we say that a node u is target to v if the distance (number of edges on the  path) is ≤ k. A node is always a target to itself.

For every node i in Tree A we may temporarily add one extra edge that connects any node of Tree A with any node of Tree B. After inserting this edge we would like to know the maximum possible number of nodes that are targets to node i in Tree A. The extra edge is removed before evaluating the next node.

Return an array answer where answer[i] is this maximum for node i.

Input Format

edges1 — n‑1 pairs [a, b] describing Tree A.

edges2 — m‑1 pairs [u, v] describing Tree B.

k       — maximum allowed distance.

2 ≤ n, m ≤ 1000, 0 ≤ k ≤ 1000.

Output Format

Return an integer array answer of length n.

Example 1

Input:
  edges1 = [[0,1],[0,2],[2,3],[2,4]]
  edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
  k = 2

Output: [9, 7, 9, 8, 8]


Example 2

Input:
  edges1 = [[0,1],[0,2],[0,3],[0,4]]
  edges2 = [[0,1],[1,2],[2,3]]
  k = 1

Output: [6, 3, 3, 3, 3]

Constraints

2 ≤ n, m ≤ 1000

0 ≤ k ≤ 1000

edges1 and edges2 form valid trees (connected, acyclic).
