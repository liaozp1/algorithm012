class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def back_track(nums, temp):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                back_track(nums, temp)
                temp.pop()
        res = []
        temp = []
        back_track(nums, temp)
        return res