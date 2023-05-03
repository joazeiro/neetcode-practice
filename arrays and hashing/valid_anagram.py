""" 
Given two strings s and t, return true if t is an anagram of s, and 
false otherwise.
An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original 
letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

""" 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_list1 = [i for i in s]
        my_list2 = [i for i in t] 

        
        my_list1.sort()
        my_list2.sort()

        if  my_list1 == my_list2:
            return True

        return False