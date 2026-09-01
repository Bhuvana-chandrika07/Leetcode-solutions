class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        startX, startY = -1, -1
        totalLitter = 0
        for row in range(m):
            for col in range(n):
                ch = classroom[row][col]
                if ch == "S":
                    startX, startY = row, col
                elif ch == "L":
                    totalLitter += 1
        
        if totalLitter == 0:
            return 0
        
        bestEnergy = {}
        initialCollected = ()

        bestEnergy[(startX, startY, initialCollected)] = energy
        q = deque([(startX, startY, initialCollected, energy, 0)])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, collected, curEne, steps = q.popleft()

            if len(collected) == totalLitter:
                return steps
            
            if curEne == 0:
                continue
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != "X":
                    cell = classroom[nr][nc]
                    nextEne = curEne - 1
                    nextCollected = collected

                    if cell == "R":
                        nextEne = energy
                    
                    elif cell == "L" and (nr, nc) not in collected:
                        nextCollected = tuple(sorted(collected + ((nr, nc), )))
                    
                    stateKey = (nr, nc, nextCollected)

                    if nextEne > bestEnergy.get(stateKey, -1):
                        bestEnergy[stateKey] = nextEne
                        q.append((nr, nc, nextCollected, nextEne, steps + 1))
        return -1


