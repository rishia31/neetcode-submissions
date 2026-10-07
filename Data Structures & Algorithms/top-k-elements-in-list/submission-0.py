from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_count = defaultdict(int)
        result = []

        for num in nums:
            hash_count[num] += 1
        
        pairs = []
        for num, count in hash_count.items():
            pairs.append((count, num))
        
        pairs.sort(reverse=True)

        for i in range (k):
            result.append(pairs[i][1])

        return result