
class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            largest = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        base = 1
        while base < n:
            base <<= 1

        seg = [0] * (2 * base)

        for u, ch in enumerate(s):
            seg[base + pos[u]] = 1 << (ord(ch) - ord('a'))

        for i in range(base - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def update(p: int, value: int) -> None:
            p += base
            seg[p] = value
            p >>= 1

            while p:
                seg[p] = seg[2 * p] ^ seg[2 * p + 1]
                p >>= 1

        def range_xor(l: int, r: int) -> int:
            l += base
            r += base
            result = 0

            while l < r:
                if l & 1:
                    result ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    result ^= seg[r]
                l >>= 1
                r >>= 1

            return result

        def path_xor(u: int, v: int) -> int:
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u] + 1)
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v] + 1)
            return result

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                c = parts[2]
                update(pos[u], 1 << (ord(c) - ord('a')))
            else:
                u = int(parts[1])
                v = int(parts[2])
                mask = path_xor(u, v)
                answer.append((mask & (mask - 1)) == 0)

        return answer