class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            current = target-nums[i]
            if current in nums and (nums.index(current)!=i):
                return [i,nums.index(current)]
            else:
                current=0