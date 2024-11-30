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




# Find a number in the array
def find_num(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            print (f"{target} is present.")
            return 
    
    print ("Target not found")
 
my_arr=[1,2,3,4,5,6,7]       
find_num(my_arr,9)


# Find the maximum product of two integers in an array where all elements are positive
def max_product(arr):
    arr.sort()
    n=len(arr)
    product= arr[n-1]*arr[n-2]
    return product


# Remove first and last element and print the middle list
def middle(lst):
    lst.pop()
    lst.pop(0)
    return lst

lst=[1,2,3,4]
print(middle(lst))


# Given a list, write a function to get first, second best scores from the list.
def first_second(my_list):
    unique_scores = list(set(my_list))
    unique_scores.sort()
    n=len(unique_scores)
    return(unique_scores[n-1],unique_scores[n-2])
   
my_list =[84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(my_list))


    
