class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        arr = [i for line in matrix for i in line]
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            if arr[mid] < target:
                l = mid + 1
            if arr[mid] > target:
                r = mid - 1
        return False
