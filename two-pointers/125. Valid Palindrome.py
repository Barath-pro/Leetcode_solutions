class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1="".join(ch.lower() for ch in s if ch.isalnum())
        if s1==s1[::-1]:
            return True
        else:
            return False