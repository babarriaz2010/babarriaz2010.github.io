

#find occurence


# nums = [11,2,3,3,4,5,3,5,24]
# numocc = {}

# for num in nums:
#     if num in numocc:
#         numocc[num]+=1
#     else:
#         numocc[num]=1

# print(numocc)


# nums = [11,2,3,3,4,5,3,5,24]

# setnums = set(nums)

# if len(nums)!= len(setnums):
#     print(f"duplicate found :) set count: {len(setnums)} and array count : {len(nums)}")
# else:
#     print("distinct values")


# nums = [1,2,4,0,5,0,7]

# nums.sort(reverse=True)

# print(nums);



# nums1 = [4, 5, 6, 0, 0, 0]
# nums2 = [1, 2, 3]

# result = nums1[:3] + nums2
# result.sort()

# print(result)


# counts = {}

# for ch in "banana":
#     counts[ch] = counts.get(ch, 0) + 1

# print(counts)


# def remove_duplicates(nums):
#     if not nums:
#         return 0

#     write = 1

#     for read in range(1, len(nums)):
#         if nums[read] != nums[read - 1]:
#             nums[write] = nums[read]
#             write += 1

#     return write


# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# k = remove_duplicates(nums)

# print(k)
# print(nums)
# print(nums[:5])    

# Traversal

# nums = [10, 20, 30, 40]
# for num in nums:
#     print(num)


#In-place Updates
# nums = [1, 2, 3]
# for i in range(len(nums)):
#     nums[i] *= 2  # Updates the original array: [2, 4, 6]    

# print(nums)



# Prefix/Suffix Arrays
# Pre-calculating cumulative results (sums, products) from left-to-right (prefix) or right-to-left (suffix) to quickly query range values.

# Python
# nums = [1, 2, 3, 4]
# # Prefix sums: running totals from the left
# prefix = [0] * len(nums)
# prefix[0] = nums[0]

# # print(range(1, len(nums)))

# for i in range(1, len(nums)):
#     prefix[i] = prefix[i - 1] + nums[i]
#     # print(prefix[i])
# # prefix is now [1, 3, 6, 10]
# # print(prefix)



# Running Sums

# A simplified form of prefix tracking where you maintain a cumulative total on the fly as you iterate.

# Python
# nums = [1, 2, 3, 4]
# running_sum = 0
# for num in nums:
#     running_sum += num
#     print(running_sum)  # Prints 1, 3, 6, 10



# Frequency Counting
# Tracking how often each element appears in an array, typically done using a dictionary or Python's Counter.

# Python
# from collections import Counter

# nums = [1, 2, 2, 3, 3, 3]
# counts = Counter(nums)
# print(counts)  # Output: 3    


# Sorting
# Arranging elements in ascending or descending order. Python uses Timsort with an average time complexity of O(n log n).

# Python
# nums = [4, 1, 3, 2]
# nums.sort()  # In-place sort: [1, 2, 3, 4]

# print(nums)



# Index Manipulation
# Using indices creatively, such as using two pointers moving toward each other or sliding a window across the array.

# Python
# Two pointers moving from opposite ends
# nums = [1, 2, 3, 4, 5]
# left, right = 0, len(nums) - 1
# while left < right:
#     print(nums[left], nums[right])
#     left += 1
#     right -= 1


# Part 2: Essential Array Problems
# 1. Two Sum
# Concept: Find two numbers that add up to a target.

# Solution: Use a hash map to store numbers and their indices as you iterate, checking if the complement (target - current) already exists.

# Python

# def twoSum(nums, target):
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i




# nums=[2,4,5,6,7,8]
# target = 9
# print(twoSum(nums,target))



# def containsDuplicate(nums):
#     return len(nums) != len(set(nums))


# nums=[2,4,5,6,7,8,2]    

# print(containsDuplicate(nums))


# Maximum Subarray (Kadane's Algorithm)
# Concept: Find the contiguous subarray with the largest sum.

# Solution: Keep a running current sum, resetting it to zero if it drops below zero, while tracking the 
# maximum sum found.

# Python
# def maxSubArray(nums):
#     max_sum = current_sum = nums[0]
#     for num in nums[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum

# nums =[3,2,-4,-3,3,4]

# maxsum = maxSubArray(nums)

# print(maxsum)



# 5. Product of Array Except Self
# Concept: Return an array where each element is the product of all other elements without using division.

# Solution: Build left (prefix) products first, then multiply them by right (suffix) products on the fly.

# Python

# def productExceptSelf(nums):
#     res = [1] * len(nums)
#     prefix = 1
#     for i in range(len(nums)):
#         res[i] = prefix
#         prefix *= nums[i]
#     suffix = 1
#     for i in range(len(nums) - 1, -1, -1):
#         res[i] *= suffix
#         suffix *= nums[i]
#     return res


# nums = [1,2,3,4,5]
# print(productExceptSelf(nums))


# Missing NumberConcept: Find the missing number in a sequence from 0 to n.Solution:
# Use the arithmetic progression sum formula ($n \times (n + 1) / 2$) and subtract the 
# sum of the array.Pythondef missingNumber(nums):
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     return expected_sum - sum(nums)


# Move Zeroes
# Concept: Move all zeros to the end while maintaining the relative order of non-zero elements in-place.

# Solution: Use a pointer to track where the next non-zero element should be placed.

# Python
# def moveZeroes(nums):
#     last_non_zero = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
#             last_non_zero += 1




# Rotate ArrayConcept: Rotate an array to the right by $k$ steps.Solution: Use Python 
# slicing to rearrange the array segments.Pythondef rotate(nums, k):
  
# def rotate(nums, k):
#     k = k % len(nums)
#     nums[:] = nums[-k:] + nums[:-k]


# Majority ElementConcept: Find the element that appears more than $n / 2$ times.Solution: 
# Boyer-Moore Voting Algorithm maintains a candidate and a counter.Python

# def majorityElement(nums):
#     count = 0
#     candidate = None
#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += 1 if num == candidate else -1
#     return candidate



# def merge(nums1, m, nums2, n):
#     p1, p2, p = m - 1, n - 1, m + n - 1
#     while p1 >= 0 and p2 >= 0:
#         if nums1[p1] > nums2[p2]:
#             nums1[p] = nums1[p1]
#             p1 -= 1
#         else:
#             nums1[p] = nums2[p2]
#             p2 -= 1
#         p -= 1
#     nums1[:p2 + 1] = nums2[:p2 + 1]



# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3

# merge(nums1, m, nums2, n)

# print(nums1)



# from collections import Counter

# def topKFrequent(nums, k):
#     count = Counter(nums)
#     return [item[0] for item in count.most_common(k)]




# nums = [1,3,4,4,3,3,2,2,2,2]

# k=1

# print(topKFrequent(nums,k))


# 5. Longest Consecutive Sequence

# def longestConsecutive(nums):
#     num_set = set(nums)
#     longest = 0
#     for n in num_set:
#         if (n - 1) not in num_set:
#             length = 1
#             while (n + length) in num_set:
#                 length += 1
#             longest = max(longest, length)
#     return longest


# nums = [3,334,42,5,4,2,1]


# print(longestConsecutive(nums))



# 6. First Unique Character
# Concept: Find the index of the first non-repeating character in a string.

# Solution: Count all characters first, then iterate through the string again to find the first one with a count of 1.

# Python

# from collections import Counter

# def firstUniqChar(s):
#     count = Counter(s)
#     for i, char in enumerate(s):
#         if count[char] == 1:
#             return i
#     return -1


# print(firstUniqChar("babar"))


# def isIsomorphic(s, t):
#     if len(s) != len(t):
#         return False
        
#     mapS, mapT = {}, {}
#     for c1, c2 in zip(s, t):
#         if (c1 in mapS and mapS[c1] != c2) or (c2 in mapT and mapT[c2] != c1):
#             return False
#         mapS[c1] = c2
#         mapT[c2] = c1
#     return True

# s = 'abc'
# t = 'sam'
# print(isIsomorphic(s, t))  # Output: False



# def isPalindrome(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         if not s[left].isalnum():
#             left += 1
#         elif not s[right].isalnum():
#             right -= 1
#         elif s[left].lower() != s[right].lower():
#             return False
#         else:
#             left, right = left + 1, right - 1
#     return True
# s = 'baab'
# print(isPalindrome(s))    


# Two Sum II (Sorted Array)
# What it is: Find two numbers in a sorted array that add up to a specific target.

# How we fix it: Start with pointers at both ends. If their sum equals the target, return their
 # 1-based indices. If the sum is too small, move the left pointer up; if it's too large, move
  # the right pointer down.


# def twoSum(numbers, target):
#     seen = {}
#     for i, num in enumerate(numbers):
#         complement = target - num
#         if complement in seen:
#             # Returning 1-based indices to match your example format
#             return [seen[complement] + 1, i + 1]
#         seen[num] = i

# numbers = [2, 4, 5, 7, 8, 6]
# target = 15

# print(twoSum(numbers, target))  # Output: [3, 5] (since numbers[2]=5 and numbers[4]=8, or indices corresponding to 7 and 8)



# def moveZeroes(nums):
#     last_non_zero = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
#             last_non_zero += 1


# nums = [1,3,4,5,5,0,0,3,4,5]

# moveZeroes(nums)

# print(nums)



# Trapping Rain Water
# What it is: Compute how much water can be trapped between bars of varying heights after it rains.

# How we fix it: Use two pointers starting at both ends along with tracking variables for 
#the maximum height seen from the left and right, adding trapped water dynamically based on the limiting shorter wall.

# Python
# def trap(height):
#     if not height:
#         return 0
#     left, right = 0, len(height) - 1
#     left_max, right_max = height[left], height[right]
#     water = 0
#     while left < right:
#         if left_max < right_max:
#             left += 1
#             left_max = max(left_max, height[left])
#             water += left_max - height[left]
#         else:
#             right -= 1
#             right_max = max(right_max, height[right])
#             water += right_max - height[right]
#     return water

# # Fixed: Pass a list/array of wall heights
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# print(trap(height))  # Output: 6


# def findMaxAverage(nums, k):
#     current_sum = sum(nums[:k])
#     max_sum = current_sum
#     for i in range(k, len(nums)):
#         current_sum += nums[i] - nums[i - k]
#         max_sum = max(max_sum, current_sum)
#     return max_sum / k




# nums = [2,3,0,1,3,2,5]
# k = 3

# print(findMaxAverage(nums,k))


# def lengthOfLongestSubstring(s):
#     char_set = set()
#     left = 0
#     max_len = 0
#     for right in range(len(s)):
#         # print(right)
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_len = max(max_len, right - left + 1)
#         print(char_set)
#     return max_len  

# c= 'abcdhdaaabbcabcdefg'
# print(lengthOfLongestSubstring(c))      



# 3. Minimum Size Subarray Sum (Dynamic Window)
# What it is: Find the minimal length of a contiguous subarray of which the sum is greater than or equal to a target.

# How we fix it: Expand right to add values to a running sum. Once the sum meets or exceeds the target, record the window length, then shrink from the left to find the smallest possible valid window.

# Python


# def minSubArrayLen(target, nums):
#     left = 0
#     current_sum = 0
#     min_len = float('inf')
#     for right in range(len(nums)):
#         current_sum += nums[right]
#         while current_sum >= target:
#             min_len = min(min_len, right - left + 1)
#             current_sum -= nums[left]
#             left += 1
#     return min_len if min_len != float('inf') else 0

# nums = [1,2,3,4,5]
# target = 13
# print(minSubArrayLen(target, nums))



# Permutation in String (Fixed Window)
# What it is: Check if one string's permutation is a substring of another string.

# How we fix it: Use frequency counters and a fixed window of size equal to the length
# of the shorter string, sliding it across the longer string while comparing character counts.

# Python
# from collections import Counter

# def checkInclusion(s1, s2):
#     len1, len2 = len(s1), len(s2)
#     if len1 > len2:
#         return False
    
#     s1_count = Counter(s1)
#     window_count = Counter(s2[:len1])
    
#     if s1_count == window_count:
#         return True
        
#     for i in range(len1, len2):
#         window_count[s2[i]] += 1
#         window_count[s2[i - len1]] -= 1
#         if window_count[s2[i - len1]] == 0:
#             del window_count[s2[i - len1]]
#         if s1_count == window_count:
#             return True
#     return False

# s1 = "cabd"
# s2 = "ceidacbcooo"
# print(checkInclusion(s1, s2))


from collections import defaultdict

def characterReplacement(s, k):
    count = defaultdict(int)
    left = 0
    max_freq = 0
    max_len = 0
    
    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])
        
        # If invalid window size, shrink from left
        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
            
        max_len = max(max_len, right - left + 1)
    return max_len

s='qabcdefgh'
k=1  
print(characterReplacement(s,k))  