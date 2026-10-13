import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        data structure:graph
        algorithm: breath first search 
        time complexity:O(Q∗(V+E))
        space complexity:O(Q∗(V+E))
        """
        
        adj = collections.defaultdict(list) 
        
        for i, eq in enumerate(equations):
            a, b = eq
            # append a tuple
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0
            if src == target:
                return 1.0
            
           
            queue, visit = collections.deque([(src, 1.0)]), {src}
            
            while queue:
                n, w = queue.popleft()
                if n == target:
                    return w
                
                for nei, weight in adj[n]:
                    if nei not in visit:
                        visit.add(nei)
                        queue.append((nei, w * weight))
            return -1.0

        return [bfs(query[0], query[1]) for query in queries]