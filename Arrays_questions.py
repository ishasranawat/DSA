1. # Missing numbers- The function takes two parameter the array and the number of elements that needs to be in array. 
def missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing= expected_sum - actual_sum
    return missing


2.# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. (Two sum)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
             for j in range(i+1, len(nums)):
                if nums[i]+ nums[j]== target:
                    return [i,j]


3.# Find a number in the array
def find_num(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            print (f"{target} is present.")
            return 
    
    print ("Target not found")
my_arr=[1,2,3,4,5,6,7]       
find_num(my_arr,9)



4.# remove duplicate numbers
def remove_duplicates(arr):
    new_arr= list(set(arr))
    return new_arr
 
arr=[1, 1, 2, 2, 3, 4, 5]  
print(remove_duplicates(arr))



5.# Find the maximum product of two integers in an array where all elements are positive
def max_product(arr):
    arr.sort()
    n=len(arr)
    product= arr[n-1]*arr[n-2]
    return product


6.# Remove first and last element and print the middle list
def middle(lst):
    lst.pop()
    lst.pop(0)
    return lst

lst=[1,2,3,4]
print(middle(lst))



7.# Given a list, write a function to get first, second best scores from the list.
def first_second(my_list):
    unique_scores = list(set(my_list))
    unique_scores.sort()
    n=len(unique_scores)
    return(unique_scores[n-1],unique_scores[n-2])
   
my_list =[84,85,86,87,85,90,85,83,23,45,84,1,2,0]
print(first_second(my_list))



8.# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result
 
arr = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target_sum = 7
print(pair_sum(arr, target_sum))



9.# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]== nums[j]:
                return True         
    return False
                
nums= [1,2,3,1]
print(contains_duplicate(nums))



10.# FIND DUPLICATE 
from sys import *
from collections import *
from math import *

def findDuplicate(arr:list, n:int):
    arr.sort()
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            return arr[i]
    return -1


11.# next greater number
from typing import List

def nextGreaterElement(arr: List[int], n: int) -> List[int]:
    result = [-1] * n  
    for i in range(n):
        
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break  
    
    return result


12.# second largest element
def findSecondLargest(sequenceOfNumbers):
    new_set=list(set(sequenceOfNumbers))
    if len(new_set) < 2:
        return -1
    n=len(new_set)
    new_set.sort()
    return new_set[n-2]




13.# rearrange alteratively
def rearrange(arr):
    # Separate positive and negative numbers
    positives = [x for x in arr if x >= 0]
    negatives = [x for x in arr if x < 0]
    
    # Initialize result array
    result = []
    # Alternate between negative and positive numbers
    for i in range(max(len(positives), len(negatives))):
        # Add negative number if available
        if i < len(negatives):
            result.append(negatives[i])
        
        # Add positive number if available
        if i < len(positives):
            result.append(positives[i])
































    
