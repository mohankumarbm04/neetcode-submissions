from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                # Use [seen[complement], idx] if 0-indexed (LeetCode 1)
                return [seen[complement] + 1, idx + 1]
            seen[num] = idx
        return []
