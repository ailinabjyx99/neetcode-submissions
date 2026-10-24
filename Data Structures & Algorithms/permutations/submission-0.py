class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        record = [False]*len(nums)
        res = []
        def backtrack(path):
            if len(path)==len(nums):
                res.append(path[:])
            for i in range(len(nums)):
                if record[i]:
                    continue
                record[i]=True
                path.append(nums[i])
                backtrack(path)
                
                record[i]=False
                path.pop()
        backtrack([])
        return res
