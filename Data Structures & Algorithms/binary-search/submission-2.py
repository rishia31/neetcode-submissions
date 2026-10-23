class Solution:
    def search(self, nums: List[int], target: int) -> int:
        count = 0
        i = 0
        for each in nums:
            if each == target:
                count += 1
                i = nums.index(each)
            else:
                count = count
        if count > 0:
            return i
        else:
            return -1 
                
        