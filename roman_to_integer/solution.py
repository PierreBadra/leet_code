from colorama import Fore

class Solution:
    symbol_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

    def romanToInt(self, s: str) -> int:
        if len(s) < 1:
            return 0
        
        if len(s) == 1:
            return self.symbol_value[s] if s in "IVXLCDM" else 0
        
        value = 0
        i = len(s) - 2

        while i >= 0:
            right = s[i + 1]
            left = s[i]
            if right and left in "IVXLCDM":
                if self.symbol_value[left] < self.symbol_value[right]:
                    value += self.symbol_value[right] - self.symbol_value[left]
                    i -= 2
                else:
                    value += self.symbol_value[right]
                    i -= 1
                
        if i == -1:
            value += self.symbol_value[s[i + 1]]

        return value
    
def main():
    solution = Solution()
    test_cases = [
        ["III", 3],
        ["LVIII", 58],
        ["MCMXCIV", 1994],
    ]
    
    for test_case in test_cases:
        answer = solution.romanToInt(test_case[0])
        if answer == test_case[1]:
            print(Fore.GREEN + "Pass")
        else:
            print(Fore.RED + f'Fail: Expected "{test_case[1]}"; got "{answer}"')
            
if __name__ == "__main__":
    main()