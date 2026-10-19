class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        output = [1] * n

        # 1. Fill prefix: product of everything to the left of i
        curr = 1
        for i in range(n):
            prefix[i] = curr
            curr *= nums[i]

        # 2. Fill postfix: product of everything to the right of j
        curr = 1
        for j in range(n - 1, -1, -1):
            postfix[j] = curr
            curr *= nums[j]

        # 3. Combine element-by-element
        for i in range(n):
            output[i] = prefix[i] * postfix[i]

        return output