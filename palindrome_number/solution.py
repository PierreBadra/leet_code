import math
from colorama import Fore

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        length = math.floor(math.log10(abs(x))) + 1
        n = 0
        initial_n = x
        for _ in range(length):
            div = math.floor(x / 10)
            mod = x % 10
            n = n * 10 + mod
            x = div

        return True if n == initial_n else False
    

def main():
    solution = Solution()
    test_cases = [
        [121, True],
        [-121, False],
        [10, False]
    ]

    for test_case in test_cases:
        answer = solution.isPalindrome(test_case[0])
        if answer == test_case[1]:
            print(Fore.GREEN + "Pass")
        else:
            print(Fore.RED + f'Fail: Expected "{test_case[1]}"; got "{answer}"')


if __name__ == "__main__":
    main()
