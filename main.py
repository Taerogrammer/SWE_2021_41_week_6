from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]
    return