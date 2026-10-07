class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        for i in range(0, len(nums)):
            for j in range (i, len(nums)):
                if i == j:
                    j += 1
                if nums[i] + nums[j] == target:
                    sol.append(i)
                    sol.append(j)
                    return sol