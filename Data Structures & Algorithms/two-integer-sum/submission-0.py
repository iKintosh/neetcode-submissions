class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        residuals = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if nums[i] in residuals.keys():
                return [residuals[nums[i]], i]
            residuals[res] = i

        