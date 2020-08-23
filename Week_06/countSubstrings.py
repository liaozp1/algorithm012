# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
#
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
#
#  示例 1:
#
#
# 输入: "abc"
# 输出: 3
# 解释: 三个回文子串: "a", "b", "c".
#
#
#  示例 2:
#
#
# 输入: "aaa"
# 输出: 6
# 说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
#
#
#  注意:
#
#
#  输入的字符串长度不会超过1000。
#
#  Related Topics 字符串 动态规划
#  👍 297 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 字符串s[i⋯j]是否为回文子串，如果是，dp[i][j]=true，如果不是, dp[i][j]=false。考虑base case，
        # 这里显而易见，当只有一个字母的时候肯定是回文子串。为什么从右下角遍历：因为在填dp表时，(i, j)
        # 位置的值依赖于（i+1,j-1），也就是当前位置的左下方。显然如果从上往下遍历，左下方的值就完全没有初始化，
        # 当然当前位置也会是错误的。但是从右下角遍历就保证了左下方的所有值都已经计算好了。
        # if s is None or s == "":
        #     return 0
        # n = len(s)
        # dp = [[False for i in range(n)] for j in range(n)]
        # result = len(s)
        #
        # for i in range(n):
        #     # base case: 只有一个字母的时候肯定是回文子串
        #     dp[i][i] = True
        # for i in range(n - 1, -1, -1):
        #     for j in range(i + 1, n):
        #         if s[i] == s[j]:
        #             if j - i == 1:
        #                 # i和j相邻的时候，当然是palindrome
        #                 dp[i][j] = True
        #             else:
        #                 # 看一下里面的substring是不是palindrome
        #                 dp[i][j] = dp[i + 1][j - 1]
        #         else:
        #             # 如果当前两个字符都对不上号，那肯定不是
        #             dp[i][j] = False
        #         if dp[i][j]:
        #             result += 1
        # return result

        res = 0
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for j in range(n):
            for i in range(j, -1, -1):
                if s[i] == s[j] and (j - i <= 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    res += 1
        return res