# Missing numbers- The function takes two parameter the array and the number of elements that needs to be in array. 
def missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    
    missing= expected_sum - actual_sum
    return missing


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. (Two sum)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
             for j in range(i+1, len(nums)):
                if nums[i]+ nums[j]== target:
                    return [i,j]

    
