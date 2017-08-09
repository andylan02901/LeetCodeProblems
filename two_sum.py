class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx_a, a in enumerate(nums):
            for idx_b in xrange(idx_a+1, len(nums)):
                b = nums[idx_b]
                if target == (a + b):
                    return [idx_a, idx_b]




if __name__ == "__main__":
    sol = Solution()
    print sol.twoSum([3, 2, 4], 6)
