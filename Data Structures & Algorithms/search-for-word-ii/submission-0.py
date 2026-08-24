class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Build Trie
        root = {}

        for word in words:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node["#"] = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node:
                return

            next_node = node[ch]

            # Complete word found
            if "#" in next_node:
                result.append(next_node["#"])
                # Remove it to avoid finding the same word again
                del next_node["#"]

            # Mark current cell as visited
            board[r][c] = "#"

            # Up
            if r > 0 and board[r - 1][c] != "#":
                dfs(r - 1, c, next_node)

            # Down
            if r + 1 < rows and board[r + 1][c] != "#":
                dfs(r + 1, c, next_node)

            # Left
            if c > 0 and board[r][c - 1] != "#":
                dfs(r, c - 1, next_node)

            # Right
            if c + 1 < cols and board[r][c + 1] != "#":
                dfs(r, c + 1, next_node)

            # Restore current cell
            board[r][c] = ch

        # Start DFS from every cell
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result