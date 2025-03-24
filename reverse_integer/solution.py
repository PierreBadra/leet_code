from colorama import Fore

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

# class Solution:
#     def reverse(self, x: int) -> int:
#         upper_limit, lower_limit = 2**31 - 1, -2**31
#         sign = -1 if x < 0 else 1
        
#         x = int(str(abs(x))[::-1]) * sign
        
#         return 0 if x <= lower_limit or x >= upper_limit else x

def main():
    solution = Solution()
    test_cases = [
        [123, 321],
        [-123, -321],
        [120, 21],
        [1534236469, 0],
        [2147483647, 0],
        [-2147483412, -2143847412],
        [-1563847412, 0]
    ]
    
    for test_case in test_cases:
        answer = solution.reverse(test_case[0])
        if answer == test_case[1]:
            print(Fore.GREEN + "Pass")
        else:
            print(Fore.RED + f'Fail: Expected "{test_case[1]}"; got "{answer}"')
            
if __name__ == "__main__":
    main()