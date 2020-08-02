class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_step = 0
        n = len(nums)
        for i in range(n):
            if i <= max_step:
                max_step = max(max_step, i + nums[i])
                if max_step >= n-1:
                    return True
        return False