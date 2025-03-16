import math


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_list = list(nums1 + nums2)
        merged_list.sort()
        middle = math.ceil(len(merged_list) / 2)
        return (
            merged_list[middle - 1]
            if len(merged_list) % 2 != 0
            else (merged_list[middle - 1] + merged_list[middle]) / 2
        )


def main():
    solution = Solution()

    median = solution.findMedianSortedArrays([1, 2], [3, 4])
    print(median)


if __name__ == "__main__":
    main()
