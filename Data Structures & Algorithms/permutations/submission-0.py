class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)

        def backtrack(path):
            # We have selected all numbers
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                # Skip numbers already used
                if used[i]:
                    continue

                # Choose
                used[i] = True
                path.append(nums[i])

                # Explore
                backtrack(path)

                # Undo choice
                path.pop()
                used[i] = False

        backtrack([])
        return result