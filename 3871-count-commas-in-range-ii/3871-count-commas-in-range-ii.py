class Solution:
    def countCommas(self, n: int) -> int:
        output: int = 0
        cur: int = 1_000
        commas: int = 1
        step: int = 0
        while cur <= n:
            next_cur: int = min(cur * 10 - 1, n)
            output += (next_cur - cur + 1) * commas
            step += 1
            if step % 3 == 0: commas += 1
            cur = next_cur + 1
        return output