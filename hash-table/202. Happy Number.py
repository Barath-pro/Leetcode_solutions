class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)

            total_sum = 0
            while n>0:
                n,digits = divmod(n,10)
                total_sum+=digits**2
            n=total_sum
        return True