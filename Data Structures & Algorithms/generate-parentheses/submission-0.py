class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def is_valid(s):
            balance = 0
            for i in s:
                if i == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return not balance
        
        def dfs(s):
            if len(s) == 2*n:
                if is_valid(s):
                    res.append(s)
                return
            dfs(s+"(")
            dfs(s+")")
        
        dfs("")
        return res