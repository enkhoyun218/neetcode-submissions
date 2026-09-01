class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}
        for item in nums:
            frequency[item] = frequency.get(item, 0) + 1

        return sorted(frequency, key=frequency.get, reverse=True)[:k]
