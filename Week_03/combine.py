class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def back_track(start, temp):
            if len(temp) == k:
                result.append(temp[:])
                return
            for i in range(start, n+1):
                temp.append(i)
                back_track(i+1, temp)
                temp.pop()
        result = []
        start = 1
        temp = []
        back_track(start, temp)
        return result