class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dataset = set(nums)

        maxlength = 0
        
        for num in dataset:
            if (num-1) not in dataset:
                current = 1
                while num+1 in dataset:
                    num +=1
                    current+=1
                maxlength = max(current, maxlength)
        
        return maxlength
