class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sum = 0
        n = len(height)
        max_left = [0]*n
        max_right = [0]*n

        for i in range(1, n-1):
            max_left[i] = max(max_left[i-1],height[i-1])

        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])

        for i in range(1, n-1):
            min_max = min(max_left[i], max_right[i])
            if min_max > height[i]:
                sum += (min_max - height[i])

        return sum

if __name__ == '__main__':
    nums = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution()
    print(s.trap(nums))