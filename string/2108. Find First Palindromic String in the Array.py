class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for ch in words:
            i=0
            j=len(ch)-1
            while i<j:
                if ch[i]!=ch[j]:
                    break
                i+=1
                j-=1
            if i>=j:
                return ch
        return ""