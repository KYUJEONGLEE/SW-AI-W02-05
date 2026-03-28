class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = [0] * 101
        # d[i] 의 뜻 : i번째 집을 털때의 최댓값을 저장하는 배열
        d[0] = nums[0]
        if len(nums) < 2:
            return d[0]
        d[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            d[i] = max(d[i-1], d[i-2] + nums[i])

        return d[len(nums)-1]
