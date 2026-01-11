# 2026/01/10
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            val = self.sumDiv(n)
            if val != -1:
                ans += val

        return ans

    def sumDiv(self, num:int)->int:
        """
        情況 1：
        n = p³，且 p 是質數

        因數：1、p、p²、p³ 
        總和：1 + p + p² + p³

        例：8 = 2³
        因數：1、2、4、8
        """
        p = round(num ** (1/3))
        if p ** 3 == num and self.isPrime(p):
            return 1 + p + p*p + p*p*p
        """
        ✅ 情況 2：
        n = p × q，且 p、q 都是不同質數

        因數：1、p、q、pq
        總和：1 + p + q + pq

        例：15 = 3 × 5
        因數：1、3、5、15（
        """
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                a, b = i, num // i
                if a != b and self.isPrime(a) and self.isPrime(b):
                    return 1 + a + b + num
                return -1
        return -1 

    def isPrime(self, num: int) -> bool:
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False

        r = math.isqrt(num)
        for i in range(3, r + 1, 2):
            if num % i == 0:
                return False

        return True
