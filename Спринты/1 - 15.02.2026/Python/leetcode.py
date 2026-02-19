# Задачи из leetcode 75 по порядку

# Блок задач Array / String
# 1768. Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        for i in range(min(len(word1), len(word2))):
            result += word1[i]
            result += word2[i]
            if i == min(len(word1), len(word2)) - 1:
                if len(word1) > len(word2):
                    result += word1[i + 1:]
                elif len(word1) < len(word2):
                    result += word2[i + 1:]
        return result

# 1071. Greatest Common Divisor of Strings

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        def gcd(len1, len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1

        return str1[:gcd(len(str1), len(str2))]
    
# 1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cnt_of_candies = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= max_cnt_of_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result
    
# 605. Can Place Flowers

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1:
                if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True       
        return False
    
# 345. Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        vowels = set('aeiouAEIOU')

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            
            while left < right and s[right] not in vowels:
                right -= 1
            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)

# 151. Reverse Words in a String
    
class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s = list(s)
        vowels = set('aeiouAEIOU')

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            
            while left < right and s[right] not in vowels:
                right -= 1
            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return ''.join(s)

# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre, post = 1, 1

        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
            res[len(nums) - i - 1] *= post
            post *= nums[len(nums) - i - 1]

        return res
    
# 334. Increasing Triplet Subsequence

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        min_1, min_2 = float('inf'), float('inf')

        for i in range(len(nums)):
            if nums[i] <= min_1:
                min_1 = nums[i]
            elif nums[i] <= min_2:
                min_2 = nums[i]
            else:
                return True
        
        return False
    
# 443. String Compression

class Solution:
    def compress(self, chars: List[str]) -> int:
        left, res = 0, 0

        while left < len(chars):
            grp_len = 1

            while left + grp_len < len(chars) and chars[left + grp_len] == chars[left]:
                grp_len += 1

            chars[res] = chars[left]
            res += 1
            if grp_len > 1:
                grp_len_str = str(grp_len)
                chars[res:res+len(grp_len_str)] = list(grp_len_str)
                res += len(grp_len_str)
            left += grp_len
        
        return res
    
# Блок задач Two Pointers
# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = len(nums)
        
        while left < right:
            if nums[left] == 0:
                zero = nums.pop(left)
                nums.append(zero)
                right -= 1
            else:
                left += 1
        
        return nums
    
# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left_s = 0
        left_t = 0

        while left_t < len(t) and left_s < len(s):
            if s[left_s] == t[left_t]:
                left_s += 1
                left_t += 1
            else:
                left_t += 1
        
        if left_s == len(s):
            return True
        else:
            return False
        
# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            if (right - left) * min(height[left], height[right]) >= max_area:
                max_area = (right - left) * min(height[left], height[right])
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
    
# 1679. Max Number of K-Sum Pairs

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[right] + nums[left] == k:
                res += 1
                left += 1
                right -= 1
            elif nums[right] + nums[left] < k:
                left += 1
            else:
                right -= 1
        
        return res
    
# Блок задач Sliding Window
# 643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum = sum(nums[:k])
        currsum = sum(nums[:k])

        for i in range(k, len(nums)):
            currsum += nums[i] - nums[i - k]
            maxsum = max(maxsum, currsum)

        return maxsum / k

# 1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiouAEIOU')
        s = list(s)
        maxv, currv = 0, 0
        left = 0

        for i in range(k):
            if s[i] in vowels:
                currv += 1
        
        maxv = max(currv, maxv)

        for j in range(k, len(s)):
            if s[left] in vowels:
                currv -= 1
            left += 1
            if s[j] in vowels:
                currv += 1
            maxv = max(maxv, currv)
        
        return maxv

# 1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left + 1
    
# 1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        k = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

        return right - left