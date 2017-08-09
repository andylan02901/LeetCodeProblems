class Solution(object):
    def twoSum(self, nums, target):
        table = dict()
        for idx, n in enumerate(nums):
            if n in table:
                return [table[n][0], idx]
            table[target-n] = (idx, n)

if __name__ == "__main__":
    sol = Solution()
    print sol.twoSum([3, 3], 6)
