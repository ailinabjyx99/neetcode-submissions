class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def helper(start, end):
            dp = [0]*(n+1)
            if start==end:
                return nums[start-1]
            dp[start] = nums[start-1]
            dp[start+1] = max(nums[start-1],nums[start])
            for i in range(start+2,end+1):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
            return dp[end]
        return max(helper(1,n-1),helper(2,n))


