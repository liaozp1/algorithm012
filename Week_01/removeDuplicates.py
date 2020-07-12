class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 0
        length = len(nums)
        for i in range(1, length):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1

if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    s = Solution()
    print(s.removeDuplicates(nums))
