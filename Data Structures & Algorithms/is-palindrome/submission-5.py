class Solution:
    def isPalindrome(self, s: str) -> bool:
        sorted_s = ""
        for i in s:
            if i.isalnum():
                sorted_s = sorted_s + i.lower()
        return sorted_s == sorted_s[::-1]