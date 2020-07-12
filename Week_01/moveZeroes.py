class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0

if __name__ == '__main__':
    nums = [9, 9, 0, 8]
    s = Solution()
    print(nums)