class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k, count = 0, 1
        for i in range(1, len(nums)):
            if nums[k] == nums[i]:
                if count < 2:
                    count += 1
                    k += 1
                    nums[k] = nums[i]
            else:
                k += 1
                nums[k] = nums[i]
                count = 1
        return k + 1