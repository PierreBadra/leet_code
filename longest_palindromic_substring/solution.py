from colorama import Fore

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand_around_center(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the valid palindrome substring

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome (single character center)
            odd_palindrome = expand_around_center(i, i)
            # Even-length palindrome (two-character center)
            even_palindrome = expand_around_center(i, i + 1)

            # Update longest palindrome found
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

# class Solution:
#     def longestPalindrome(self, s: str) -> str:        
#         if len(s) == 1 or  s.lower()[::-1] == s.lower():
#             return s
        
#         palindromes = []
#         left_index = 0
#         right_index = 0
#         for right, _ in enumerate(s):
#             right_index = right
#             if left_index < right_index:
#                 if s[left_index] == s[right_index]:
#                     substr = s[left_index : right_index + 1]
#                     is_palindrome = substr.lower()[::-1] == substr.lower()
#                     if is_palindrome:
#                         palindromes.append(substr)
#                     else:
#                         left_index += 1

#         if not palindromes and len(s) != 2:
#             return self.longestPalindrome(s[left_index+1:right_index +1])
#         elif not palindromes and len(s) == 2:
#             return s[0]
        
#         return max(palindromes, key=len)


def main():
    solution = Solution()
    test_cases = [
        ["babad", "bab"],
        ["cbbd", "bb"],
        ["ac", "a"],
        ["ccc", "ccc"],
        ["abb", "bb"],
        ["aacabdkacaa", "aca"],
        ["xaabacxcabaaxcabaax", "xaabacxcabaax"],
        ["civic", "civic"]
    ]
    
    for test_case in test_cases:
        answer = solution.longestPalindrome(test_case[0])
        if answer == test_case[1]:
            print(Fore.GREEN + "Pass")
        else:
            print(Fore.RED + f'Fail: Expected "{test_case[1]}"; got "{answer}"')


if __name__ == "__main__":
    main()
