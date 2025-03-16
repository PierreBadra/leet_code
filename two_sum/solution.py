class Solution(object):    
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            nums[nums.index(num)] = ""
            x =  target - num
            if x in nums:
                return [i, nums.index(x)]
            
            nums[nums.index("")] = num
        return []


def main():
    solution = Solution()

    nums = [2, 7, 11, 15]
    answer = solution.twoSum(nums, 9)
    print(answer)

    nums = [3, 2, 4]
    answer = solution.twoSum(nums, 6)
    print(answer)

    nums = [3, 3]
    answer = solution.twoSum(nums, 6)
    print(answer)

    nums = [3, 2, 3]
    answer = solution.twoSum(nums, 6)
    print(answer)

    nums = [0, 4, 3, 0]
    answer = solution.twoSum(nums, 0)
    print(answer)

    nums = [-3, 4, 3, 90]
    answer = solution.twoSum(nums, 0)
    print(answer)


if __name__ == "__main__":
    main()
