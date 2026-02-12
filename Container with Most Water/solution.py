from colorama import Fore


class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_a = 0
        l = 0
        r = len(height) - 1
        while l < r:
            lh = height[l]
            rh = height[r]
            w = r - l
            a = w * min(lh, rh)

            if a > max_a:
                max_a = a

            if lh < rh:
                l += 1
            else:
                r -= 1

        return max_a


def main():
    solution = Solution()
    test_cases = [
        [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
        [[1, 1], 1],
    ]

    for test_case in test_cases:
        answer = solution.maxArea(test_case[0])
        if answer == test_case[1]:
            print(Fore.GREEN + "Pass")
        else:
            print(Fore.RED + f'Fail: Expected "{test_case[1]}"; got "{answer}"')


if __name__ == "__main__":
    main()
