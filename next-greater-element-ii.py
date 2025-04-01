# Time : O(4n)
# Space O(n)
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n # O(n)
        stack = []
        for i in range(2*n): #O(2n)
            if nums[(i+1)%n] > nums[(i%n)]:
                result[i%n] = nums[(i+1)%n]
                while len(stack) > 0 and nums[(i+1)%n] > nums[stack[-1]]: # O(n)
                    result[stack.pop()] = nums[(i+1)%n]
            elif i < n:
                stack.append(i)
        return result