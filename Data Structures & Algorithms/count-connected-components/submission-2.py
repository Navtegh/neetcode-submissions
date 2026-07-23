class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodecheck=[False]*n
        visited=set()
        adj=[[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            nodecheck[node]=True
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)

        count=0
        for u,v in edges:
            if nodecheck[u] or nodecheck[v]:
                continue
            else:
                count+=1
                dfs(u)
        for i in range(n):
            if not nodecheck[i]:
                count+=1
        return count