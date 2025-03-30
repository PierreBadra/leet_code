# String to Integer (atoi)

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

The algorithm for `myAtoi(string s)` is as follows:

1. Whitespace: Ignore any leading whitespace (`" "`).

2. Signedness: Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.

3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.

4. Rounding: If the integer is out of the 32-bit signed integer range `[-2^31, 2^31 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-2^31` should be rounded to `-2^31`, and integers greater than `2^31 - 1` should be rounded to `2^31 - 1`.

Return the integer as the final result.

## Examples

```python
# Example 1: s = "42"
output = solution.myAtoi(s)
# output = 42

# Explanation:
# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)
```

```python
# Example 2: s = " -042"
output = solution.myAtoi(s)
# output = -42

# Explanation:
# Step 1: " -042" (leading whitespace is read and ignored)
#             ^
# Step 2: " -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: " -042" ("042" is read in, leading zeros ignored in the result)
```

```python
# Example 3: s = "1337c0d3"
output = solution.myAtoi(s)
# output = 1337

# Explanation:
# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
```

```python
# Example 4: s = "0-1"
output = solution.myAtoi(s)
# output = 0

# Explanation:
# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
#           ^
```


```python
# Example 5: s = "words and 987"
output = solution.myAtoi(s)
# output = 0

# Explanation:
# Reading stops at the first non-digit character 'w'.
```

## Constraints

`0 <= s.length <= 200`

`s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.`

## My approach

My appraoch begins by removing any leading whitespace from the input string. Then, it checks if the string starts with a `‘+’` or `‘-’` `sign` to determine whether the resulting number should be positive or negative. This is done by checking if the `sign` character is at the beginning of the string. The function then iterates through the string, character by character, collecting numeric digits into a temporary string called `number`. It skips the `sign` character if it’s at the start and stops parsing as soon as it encounters a non-digit character.

Once the numeric portion is extracted, the function converts it to an integer and applies the previously determined sign. It then ensures the result fits within the 32-bit signed integer range (from `-2^31` to `2^31 - 1`). If the result exceeds these bounds, it is clamped to the nearest limit. Finally, the function returns the processed integer.

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        lower_limit, upper_limit = -2**31, 2**31 - 1
        s = str.lstrip(s)
        i = 0
        
        if "-" in s and s.index("-") == 0:
            sign = -1
        elif "+" in s and s.index("+") == 0 and "-" not in s:
            sign = 1
        else:
            sign = 1
        

        number = ""
        while i < len(s):
            if  s[i] == "-" and i == 0 or s[i] == "+" and i == 0:
                i += 1
                continue

            if not str.isnumeric(s[i]) or s[i] == "-" and i != 0:
                break

            number += s[i]
            i += 1
        
        result = int(number) * sign if len(number) > 0 else 0
        
        if result < lower_limit:
            return lower_limit
        
        if result > upper_limit:
            return upper_limit           

        return result
```

## A More Optimal Approach

A more optimal approach was to also first strip the input string from any leading or trailing whitespace, initialize the `i` and `res` variables to `0` and a `sign` variable to 1.

The function then iterates through each character in the string using a `for` loop. On the first character (`i == 0`), it checks for a ‘+’ or ‘-’ sign to determine the number’s polarity and updates the `sign` variable accordingly. If the character is not a digit and not a sign at the start, the loop breaks immediately.

For each digit encountered, the function multiplies the current `res` by 10 and adds the new digit. Before doing so, it checks whether this operation would cause an overflow beyond the 32-bit signed integer limit (`2^31`). If an overflow is detected, it sets `res` to `2^31` and breaks the loop early. Finally, the function returns the result, clamping it to `2^31 - 1` if the number is positive and exactly `2^31`, since that would exceed the maximum allowed value.

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        i = 0
        res = 0
        sign = 1
        for i in range(len(s)):
            if i == 0 and s[i] in "+-":
                if s[i] == "-": sign = -1
                if s[i] == "+": sign = 1
                continue
            if not s[i].isdigit():
                break
            if (res * 10) >= 2 ** 31 or res *10 + int(s[i]) >= 2 ** 31:
                res = 2 ** 31
                break
            res = (res * 10) + int(s[i])
        return 2 ** 31 - 1 if (res == 2**31 and sign == 1) else sign * res
```
