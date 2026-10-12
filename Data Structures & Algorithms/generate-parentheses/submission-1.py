class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(curr))
                return
            if openN < n:
                curr.append("(")
                backtrack(openN + 1, closedN)
                curr.pop()
            if closedN < openN:
                curr.append(")")
                backtrack(openN, closedN + 1)
                curr.pop()
        
        backtrack(0, 0)
        return res