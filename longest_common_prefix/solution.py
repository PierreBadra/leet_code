from colorama import Fore

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_prefix = ""
        loop_num = min(len(string) for string in strs) * len(strs)
        current_list_index = 0
        current_character_index = 0
        previous_character = ""
        
        for i in range(loop_num):
            if i != 0 and current_list_index != 0 and previous_character != strs[current_list_index][current_character_index]:
                break
            
            previous_character = strs[current_list_index][current_character_index]

            if current_list_index == len(strs) - 1:
                common_prefix += previous_character
                current_character_index += 1
                current_list_index = 0
            else:
                current_list_index += 1

        return common_prefix
    

def main():
    solution = Solution()
    test_cases = [
        [["flower","flow","flight"], "fl"],
        [["dog","racecar","car"], ""],
    ]
    
    for test_case in test_cases:
        answer = solution.longestCommonPrefix(test_case[0])
        if answer == test_case[1]:
            print(Fore.GREEN + "Pass")
        else:
            print(Fore.RED + f'Fail: Expected "{test_case[1]}"; got "{answer}"')
            
if __name__ == "__main__":
    main()