from typing import List
class Solution:

    def make_graph(self,edges):
        n = len(edges)+1
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        return n,graph
    
    def get_k_count(self, graph,k):

        n = len(graph)
        k_count = []
        for i in range(n):
            k_count.append(self.get_k_distance_nodes_count(i,-1,0,k,graph))
        
        return k_count
    
    def get_k_distance_nodes_count(self,node,parent,level,k,graph):

        if level == k+1:
            return 0
        
        count = 1
        for neighbour in graph[node]:
            if neighbour!=parent:
                count += self.get_k_distance_nodes_count(neighbour,node,level+1,k,graph)
        return count

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """
        0-1-2

        k_nodes_dist[0] = [1,1,1]
        k_node_dist[1] = [2,3,2]
        k_node_dist[2] = [3,3,3]

        k_node_dist[k][i] + k_node_dist[k-1][i]
        max(k_node_dist[k-1])
        why will it work?

        given a graph number of nodes in k node is fixed so we cant change it because source is fixed and edges are fixed
        Now we want maximum amount of nodes to be target from source noe in tree 1. We can attach a child node from tree 1 from source node which is within distance k but that would reduce number of possible edges for nodes in tree 2
        For optimality we would want k-1 edges to be traversable in tree 2 so we would directly link source node to tree 2 itself. Now we would want to select the node which has maximal nodes reachable of distance k-1 always to be the connector node. if we didnt choose that for any node i can choose it and it will be maximal in nature.
        How to write it as a short proof? by conttadiction?

        Lets try for the examples and see if logic is correct


        exampel 1-> k_node_dist_1 = [5,3,5,4,4]
                    k-1_node_dist_2 = [4,3,3,1,4]
                    [9,7,9,8,8]
        Looks like logic is solid but dont have proof i.e correctness and completness 
        to prove we need to show 
        0 dist nodes  <  1 dist nodes < 2 dist <k-1 < k nodes 
        which then paves way for saying choose k-1 always instead of connecting a different node other than source from trr1 which give k-2 or less in tree 2 
        so choose k-1 => choose source same as node we are computing max coutn for 
        """
        n,graph_1 = self.make_graph(edges1)
        m,graph_2 = self.make_graph(edges2)
        
        
        k_count_graph_1 = self.get_k_count(graph_1,k)
        k_minus_1_count_graph_2 = self.get_k_count(graph_2,k-1)
        max_to_add = max(k_minus_1_count_graph_2)
        for i in range(n):
            k_count_graph_1[i] += max_to_add

        return k_count_graph_1



"""
AI Commentary and Refactoring Notes
===================================

This guide highlights potential improvements to naming, structure, style,
and algorithmic efficiency in the current implementation. Use it as a
checklist when revisiting or rewriting the solution.

Part A — Code Quality & Refactoring
-----------------------------------

1. Naming & Structure
   • Consider renaming `get_k_distance_nodes_count` to `dfs_count_within_k`
     and nesting it inside `get_k_count` to narrow its scope.
   • Re-evaluate whether returning both `n` and `graph` from `make_graph`
     is necessary, since `n = len(graph)` can be inferred later.

2. Functional Style vs. Imperative
   • Some `for` loops that build lists could be replaced with list
     comprehensions for clarity and conciseness.
   • `enumerate` may improve readability when looping with indices.

3. Early Exits
   • Handle trivial cases (e.g., `k == 0` or `k < 0`) with early returns
     instead of entering DFS.

4. Type Hints & Imports
   • Add full type annotations (parameters and return types) to support
     static analysis.
   • Consider using `deque` or iterative DFS to avoid deep recursion.

5. Recursion vs. Iteration
   • Converting recursive DFS to an explicit stack may prevent recursion‐
     limit issues on skewed trees.

6. Constants & Repeated Expressions
   • Define a local constant (e.g., `MAX_DIST = k + 1`) to avoid repeated
     computation.

7. Documentation & Comments
   • Example or proof discussions may be better placed in a module-level
     docstring, keeping function docstrings concise and practical.

8. Formatting & PEP-8
   • Ensure two blank lines between top-level function definitions.
   • Evaluate whether variable names like `max_to_add` could be made more
     descriptive, e.g., `bridge_bonus`.

9. Logging vs. Print
   • Replace diagnostic `print` statements with a configurable logger.

10. Return Value Mutation
   • Consider replacing in-place updates with clearer constructs, e.g.,
     `result = [x + bonus for x in counts]`.

Part B — Algorithmic Alternatives & Design Trade-offs
-----------------------------------------------------

1. Two-Pass Tree DP
   • A bottom-up and top-down DP approach could compute counts of nodes
     within distance ≤ k for all roots in `O(n·k)` instead of performing
     DFS from every node.

2. Centroid Decomposition
   • Decomposing the tree into centroids yields `O(n log n + n·k)` runtime,
     with increased implementation complexity but improved scaling when
     `k ≪ n`.

3. Bitmask Convolution
   • Depth-frequency arrays may be represented as bitmasks, allowing depth
     merges via bit shifting (≈ `k/64` operations). Potentially useful if
     performance is critical.

4. Mo’s Algorithm on Trees
   • If answering many queries with different `k`, consider Euler Tour +
     Mo’s algorithm. Beneficial only when the number of queries is large.

5. APSP Overhead
   • All-pairs shortest paths on a tree is `O(n²)` and typically unnecessary
     unless multiple distance-based queries must be answered frequently.

6. Bridge Choice Logic
   • Evaluate whether selecting the global `(k-1)` max in Tree B is always
     optimal. A proof-by-contradiction can settle correctness assumptions.

7. Space vs. Time
   • Current memory footprint is `O((n + m)·k)`. Determine whether this is
     acceptable or if streaming / recomputation trade-offs are preferable.

Use these points as a reference when refining clarity, efficiency, and
maintainability of the code.
"""
