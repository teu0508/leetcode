'''
Time complexity O(n^2)

Since we need three numbers adding to zero, we can sort the list --O(n * log(n))
Now that we have the list sorted we define our first variable to iterate over the list 
Our other two variables for the sum will iterate from left and right accordingly to the result of the sum
    If the sum is too big the right variable iterates one position backward
    If the sum is too small the left variable iterates one position forward
    If the sum of our two variables match our goal we add that trio to our answer list
    Until j < k is not true anymore
'''



import sys

def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        ans = []
        prev = sys.maxsize
        for i in range(len(nums)-2):
            goal = -nums[i]
            if nums[i] > 0:
                return ans 
            if nums[i] == prev:
                continue
            j = i + 1
            k = len(nums)-1
            prev = nums[i]
            while j < k:
                if nums[j] + nums[k] > goal:
                    k -= 1
                elif nums[j] + nums[k] < goal:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
        return ans
    
def threeSum_2(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i, a in enumerate(nums):
            if a > 0:
                return ans
            if i > 0 and a == nums[i-1]:
                continue
            
            j, k = i + 1, len(nums)-1

            while j < k:
                three_sum = a + nums[k] + nums[j]
                if three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    ans.append([a, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j+= 1
        return ans