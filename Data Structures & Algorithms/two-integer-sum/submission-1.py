class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for index,value in enumerate(nums):
            data[value] = index
        ans = []
        for index,value in enumerate(nums):
            if (target-value) in data and data[target-value]!=index:
                return [index,data[target-value]]


        
        
        