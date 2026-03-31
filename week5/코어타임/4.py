class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        row = len(triangle)
        col = len(triangle[-1])

        dp = [[0] * row for _ in range(col)]
        # print(dp)

        dp[0][0] = triangle[0][0]
        # print(dp[0][0])
        for i in range(1, row):
            col = len(triangle[i])
            for j in range(col):
                if j - 1 < 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == col - 1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

        # print(dp)
        return min(dp[row-1])
