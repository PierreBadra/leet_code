class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


def main():
    test_inputs = ["abcabcbb", "bbbbb", "pwwkew", " ", "dvdf"]
    solution = Solution()

    for input in test_inputs:
        length = solution.lengthOfLongestSubstring(input)
        print(length)


if __name__ == "__main__":
    main()
