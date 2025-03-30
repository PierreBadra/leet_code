from colorama import Fore

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


def main():
    solution = Solution()
    test_cases = [
        ["42", 42],
        [" -042", -42],
        ["1337c0d3", 1337],
        ["0-1", 0],
        ["words and 987", 0],
        ["-91283472332", -2147483648],
        ["-+12", 0],
        ["  -0012a42", -12],
        ["-13+8", -13]
    ]

    for test_case in test_cases:
        answer = solution.myAtoi(test_case[0])
        if answer == test_case[1]:
            print(Fore.GREEN + "Pass")
        else:
            print(Fore.RED + f'Fail: Expected \n"{test_case[1]}"; got \n"{answer}"')


if __name__ == "__main__":
    main()
