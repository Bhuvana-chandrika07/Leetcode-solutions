class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if not beginWord or not endWord or endWord not in wordList or beginWord == endWord:
            return []
        nei = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                nei[pattern].append(word)
        que = collections.deque([beginWord]) # beginword, moves
        visited = {beginWord}
        parents = defaultdict(list)
        found = False
        while que and not found:
            localvisited = set()
            qlen = len(que)
            for _ in range(qlen):
                word = que.popleft()
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            if neiWord == endWord:
                                found = True
                            if neiWord not in localvisited:
                                que.append(neiWord)
                                localvisited.add(neiWord)
                            parents[neiWord].append(word)
            visited.update(localvisited) #union

        res = []
        def DFS(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for parent in parents[word]:
                DFS(parent, path + [parent])
        if found:
            DFS(endWord,[endWord])
        
        return res