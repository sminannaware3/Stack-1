# Time O(2n)
# Space O(n)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n
        for i in range(n-1):
            if temperatures[i+1] > temperatures[i]:
                result[i] = 1
                while len(stack) > 0 and temperatures[i+1] > temperatures[stack[-1]]:
                    j = stack.pop()
                    result[j] = i+1 - j
            else:
                stack.append(i)
        return result
            