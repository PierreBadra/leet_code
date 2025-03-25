# Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

## Examples

```python
# Example 1: s = "PAYPALISHIRING", numRows = 3
output = solution.convert("PAYPALISHIRING", 3)
# output = "PAHNAPLSIIGYIR"
```

```python
# Example 2: s = "PAYPALISHIRING", numRows = 4
output = solution.convert("PAYPALISHIRING", 4)
# output = "PINALSIGYAHRPI"

# Explanation:
# P     I      N
# A   L S    I G
# Y A   H  R
# P     I
```

```python
# Example 3: s = "A", numRows = 1
output = solution.convert("A", 1)
# output = "A"
```

## Constraints

`1 <= s.length <= 1000`

`s consists of English letters (lower-case and upper-case), ',' and '.'`

`1 <= numRows <= 1000`

## My approach

My approach begins by handling edge cases—if `numRows` is 1 or the length of `s` is 1, the function immediately returns `s` since no zigzag transformation is necessary.

Next, a 2D list (`Matrix`) is created with `numRows` rows and `numCols` set to the length of `s`, initializing all elements with spaces. The traversal starts by initializing `currRow`, `currCol`, and `i` to 0. As the function iterates through the string `s`, it places characters in the matrix while moving downward through the rows.

Once the last row is reached, the movement switches to a diagonal upward-right direction. This zigzag pattern continues until all characters are placed in the matrix. Finally, the function constructs the output string by concatenating all non-space characters from each row, forming the final transformed result.

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s

        numCols = len(s)
        Matrix = [[" " for _ in range(numCols)] for _ in range(numRows)]

        currRow = 0
        currCol = 0
        i = 0
        while i < len(s) and currCol < numCols:
            if currCol != 0 and currRow == 0:
                currRow += 1

            if currRow < numRows:
                Matrix[currRow][currCol] = s[i]
                currRow += 1
                i += 1
            else:
                currRow -= 1
                while currRow != 0 and i < len(s):
                    currRow -= 1
                    currCol += 1
                    if currCol >= numCols:
                        break
                    Matrix[currRow][currCol] = s[i]
                    i += 1

        converted_string = ""

        for row in Matrix:
            converted_string += str.strip("".join(row)).replace(" ", "")

        return converted_string
```

## A More Optimal Approach

A more optimal solution begins by handling an edge case—if `numRows` is 1, the function immediately returns `s` since no zigzag transformation is necessary.

Next, a list `res` is initialized with `numRows` empty strings, where each element represents a row in the zigzag pattern. The `place` variable, which tracks the current row, is initialized to 0, and the `down` variable, which determines the traversal direction, is set to `True`.

The function then iterates through each character `c` in `s`, appending it to the corresponding row in `res` based on the current value of `place`. If `place` reaches the last row (`numRows - 1`), the direction switches upward by setting `down` to `False`. If `place` reaches the first row (`0`), the direction switches downward by setting `down` to `True`. Depending on the value of `down`, `place` is either incremented (moving downward) or decremented (moving upward).

Once all characters have been placed in their respective rows, the function joins all elements of `res` into a single string and returns the final zigzag-transformed result.

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res = [""]*numRows
        place = 0
        down = True

        for c in s:
            res[place] += c
            if place == numRows -1:
                down = False

            if place == 0:
                down = True

            if down:
                place += 1
            else:
                place -= 1

        return "".join(res)
```
