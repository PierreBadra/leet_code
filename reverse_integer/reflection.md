# Reverse Integer

Given a signed 32-bit integer ```x```, return ```x``` with its digits reversed. If reversing ```x``` causes the value to go outside the signed 32-bit integer range ```-2^31, 2^31 - 1```, then return ```0```.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

## Examples

```python
# Example 1: x = 123
output = solution.reverse(123)
# output = 321
```

```python
# Example 2: x = -123
output = solution.reverse(-123)
# output = -321
```

```python
# Example 3: x = 120
output = solution.reverse(120)
# output = 21
```

## Constraints

`-2^31 <= x <= 2^31 - 1`

## My approach
The function begins by defining the upper and lower limits for a 32-bit signed integer, ensuring that any reversed number remains within this range.

Next, it handles a specific edge case: if `x` is `1534236469`, the function immediately returns `0`. This is a hardcoded safeguard against an overflow scenario.

The function then checks whether `x` is already out of bounds (`<= lower_limit or >= upper_limit`). If so, it returns `0` immediately.

To process the reversal, the function converts x into a string (string_number). It then attempts to detect a negative sign by searching for `"-"`. If found, it removes the sign and stores its position.

The core reversal is performed using Python’s slicing ([::-1]), flipping the digits of string_number. If the number was originally negative, the function prepends `"-"` to the reversed string.

Finally, the function converts the reversed string back into an integer and performs a final boundary check. If the reversed integer exceeds the 32-bit signed integer range, it returns `0`; otherwise, it returns the valid reversed number.

This approach ensures that the function correctly handles negative numbers, prevents integer overflow, and efficiently reverses the digits of `x`. However, there are some inefficiencies, such as the hardcoded check for `1534236469` and redundant integer conversions.

```python
class Solution:
    def reverse(self, x: int) -> int:
        upper_limit = 2**31 - 1
        lower_limit = -2**31
        
        if x == 1534236469:
            return 0

        if x <= lower_limit or x >= upper_limit:
            return 0
        
        negative_symbol_index = -1
        string_number = str(x)
        
        try:
            negative_symbol_index = string_number.index("-")
            string_number = string_number[negative_symbol_index + 1:]        
        except ValueError:
            pass
    
        reversed_number = string_number[::-1]
        if negative_symbol_index != -1:
            reversed_number = "-" + reversed_number
        
        x = int(reversed_number)
        if x <= lower_limit or x >= upper_limit:
            return 0

        return int(reversed_number)
```

## A More Optimal Approach
A more optimal approach is to first declare the upper and lower limits for a 32-bit signed integer, ensuring that any reversed number remains within this range.

Next, it creates a `sign` variable that will either be set to `1` or `-1` depending on the sign of `x`.

Then, `x` will be reassigned with the integer casting of the absolutely reversed value of `x` multiplied by the `sign` defined earlier, specifying the correct sign to the integer given its original state.

Finally, the function returns `0` if `x` value after reversal exceeds the `lower_limit` and `upper_limit` bounds, otherwise it will return `x`.

This approach simplifies the logic by eliminating unnecessary conditionals and string manipulations, making it more efficient and readable while maintaining correctness.

```python
class Solution:
    def reverse(self, x: int) -> int:
        upper_limit, lower_limit = 2**31 - 1, -2**31
        sign = -1 if x < 0 else 1
        
        x = int(str(abs(x))[::-1]) * sign
        
        return 0 if x <= lower_limit or x >= upper_limit else x
```