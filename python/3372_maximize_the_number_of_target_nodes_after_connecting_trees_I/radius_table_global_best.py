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