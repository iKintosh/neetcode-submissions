class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['(', '{', '[']
        closed = [')', '}', ']']
        ref_closed_opened = {')' : '(', '}': '{', ']': '['}
        stack = []
        cnt = 0

        for symbol in s:
            if symbol in opened:
                stack.append(symbol)
                cnt += 1
            elif cnt>0 and symbol in closed and ref_closed_opened[symbol] == stack[cnt-1]:
                del stack[cnt-1]
                cnt -= 1
            else: 
                return False
        if cnt == 0:
            return True
        return False