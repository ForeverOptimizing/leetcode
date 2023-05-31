"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?



TIME LIMIT 30 min




"""

# class Solution(object):
#     def isAnagram(self, s, t):
#         new_string = ""
#         for char in s:
#             if char not in t:
#                 return False
#             else:
#                 new_string += char



# class Solution(object):
#     def isAnagram(self, s, t):
#         for char1 in s:
#             for char2 in t:
                


test_string = "abacbdbe"
print(test_string)












# This checks for palindrome oops

# class Solution(object):
#     def isAnagram(self, s, t):
#         print(s)
#         rev = ""
#         i = -1
#         for letter in s:
#             rev = rev + s[i]
#             print(s[i])
#             i = i - 1

#         print(rev)
#         print(s)
#         print(t)

#         return rev == t


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))





        # :type s: str
        # :type t: str
        # :rtype: bool
