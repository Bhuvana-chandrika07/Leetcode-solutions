class Solution:
    def remainingMethods(self, n: int, k: int, invocations: list[list[int]]) -> list[int]:

        # Build graph
        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        # Find suspicious methods
        suspicious = set()

        def dfs(node):
            if node in suspicious:
                return
            
            suspicious.add(node)

            for nxt in graph[node]:
                dfs(nxt)

        dfs(k)

        # Check if any outside method calls suspicious method
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))

        # Remove suspicious methods
        ans = []

        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans