"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
#Solution1: Brute Force
#This Solution Beats 14% Of other submissions in case of Runtime
# And 37% in case of Memory
"""class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[j]==target - nums[i]):
                    return [i,j]
"""
#Solution2: Two-pass Hash Table
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            dictionary = {}
            for i in range(len(nums)):
                dictionary[i] = nums[i]
            for i in range(len(nums)):
                complement = target - nums[i]
                if(complement in dictionary.values()):
                    compkey=list(dictionary.keys())[list(dictionary.values()).index(complement)]
                if (complement in dictionary.values() and compkey != i):
                    return [i,compkey]
"""
#Soltuin3: One-pass hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         dictionary = {}
         for i in range(len(nums)):
                complement = target - nums[i]
                if(complement in dictionary.values()):
                    compkey=list(dictionary.keys())[list(dictionary.values()).index(complement)]
                    return [compkey,i]    
                dictionary[i] = nums[i]
