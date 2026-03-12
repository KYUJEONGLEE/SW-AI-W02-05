class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 재귀 종료 조건 n == 0일때, x^n 에서 x에 어떤수가 들어와도 1
        if n == 0:
            return 1

        # n 이 음수일때, x^(-n) => 1 / x^n => x을 분수로, n을 양수로
        if n < 0:
            x = 1 / x
            n = -n
        # n이 양수일때, 짝수와 홀수로 나눔
        if n > 0:
            # 짝수 일떄, x^n = x^(n//2)^2
            if n % 2 == 0:
                half = self.myPow(x, n // 2)
                return half * half

            # 홀수 일때, x^n = x^(n//2)^2 * x
            elif n % 2 != 0:
                half = self.myPow(x, n // 2)
                return half * half * x
