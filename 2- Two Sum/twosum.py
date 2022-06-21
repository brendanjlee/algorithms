class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {} # index:complement_value
        
        for i in range(len(nums)):
            compl = target - nums[i]
            
            if compl in m:
                return [m[compl], i]
            
            m[nums[i]] = i
        
        return []