# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
#  示例:
#
#  输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
#  Related Topics 动态规划
#  👍 511 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        max_size = 0
        dp = [[0]*len(line) for line in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_size = max(max_size, dp[i][j])
        return max_size**2