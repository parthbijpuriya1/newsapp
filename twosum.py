class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked={}
        for k, num in enumerate(nums):
            if (target - num) in checked:
                return [checked[target - num], k]
            checked[num] = k
