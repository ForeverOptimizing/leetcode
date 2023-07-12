"""
217. Contains Duplicate - EASY
https://leetcode.com/problems/contains-duplicate/

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 
Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution(object):
    def containsDuplicate(self, nums):
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


newSolution = Solution()
exampleList = [1,1,1,3,3,4,3,2,4,2]
print(newSolution.containsDuplicate(exampleList))
































"""
# My Solution 5/27/23
# This works, but it sorts the example list in the end
# EDIT: This actually fails with negative numbers

class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        setnums = set(nums)
        listnums = list(setnums)
        return listnums != nums

        # :type nums: List[int]
        # :rtype: bool



newSolution = Solution()
exampleList = [1,3,4,2]
print(newSolution.containsDuplicate(exampleList))
"""


























# NeetCode Solution
# https://youtu.be/3OamzN90kPg

# class Solution(object):
#      def containsDuplicate(self, nums: List[int]) -> bool:
#             hashset = set()

#             for n in nums:
#                 if n in hashset:
#                     return True
#                 hashset.add(n)
#             return False



"""
First Attempt
    Upon further inspection it messes up if you have the list out of order without duplicates
    Possible solution is to sort the list of nums somehow before the comparing the lists

class Solution(object):
    def containsDuplicate(self, nums):
        
        setnums = set(nums)
        listnums = list(setnums)
        return listnums != nums

        # :type nums: List[int]
        # :rtype: bool



newSolution = Solution()
exampleList = [1,3,4,2]
print(newSolution.containsDuplicate(exampleList))


# exnums = [1,2,3,1]
# setnums = set(exnums)
# exnums2 = list(setnums)
# print(exnums==exnums2)

"""