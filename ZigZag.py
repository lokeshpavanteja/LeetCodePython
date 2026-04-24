class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        going_down = False

        for char in s:
            rows[current_row] += char

            # Change direction at top/bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down

            current_row += 1 if going_down else -1

        return "".join(rows)


# Example run
s = "PAYPALISHIRING"
numRows = 3

sol = Solution()
print("Input:", s, ", rows =", numRows)
print("Output:", sol.convert(s, numRows))