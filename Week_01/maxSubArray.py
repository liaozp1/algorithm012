class Solution:
    def maxSubArray(self, nums):
        submax=0
        maxum=nums[0]
        for i in nums:
            if submax>0:
                submax=submax+i
            else:
                submax=i
            maxum = max(maxum,submax)
        return maxum

if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(nums))
