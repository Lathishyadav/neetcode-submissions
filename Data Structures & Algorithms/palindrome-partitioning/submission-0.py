class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, path):
            # Entire string has been partitioned
            if start == len(s):
                result.append(path.copy())
                return

            # Try every possible substring
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    # Choose
                    path.append(s[start:end + 1])

                    # Explore
                    backtrack(end + 1, path)

                    # Undo
                    path.pop()

        backtrack(0, [])
        return result