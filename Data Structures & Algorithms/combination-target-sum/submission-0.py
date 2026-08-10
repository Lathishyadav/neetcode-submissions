class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        combination = []

        def backtrack(start, remaining):

            if remaining == 0:
                result.append(combination.copy())
                return

            if remaining < 0:
                return

            for i in range(start, len(nums)):

                if nums[i] > remaining:
                    continue

                combination.append(nums[i])

                backtrack(i, remaining - nums[i])

                combination.pop()

        backtrack(0, target)

        return result