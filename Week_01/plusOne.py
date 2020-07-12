class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            elif digits[i] != 9:
                digits[i] += 1
                return digits
        result = [0]*(n+1)
        result[0] = 1
        return result


if __name__ == '__main__':
    nums = [9, 9, 9, 9]
    s = Solution()
    print(s.plusOne(nums))