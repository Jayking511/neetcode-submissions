class Solution:
    def isPalindrome(self, s: str) -> bool:
        sorted_s = ""
        for i in s:
            if i.isalnum():
                sorted_s = sorted_s + i.lower()
        ispal = True
        for i in range(len(sorted_s)):
            if sorted_s[i] != sorted_s[len(sorted_s)-1-i]:
                ispal = False
                break
        return ispal
