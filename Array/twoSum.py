class Solution:
    def twoSumHash(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if (target - nums[i]) in d.keys():
                return [d[target-nums[i]], i]
            d[nums[i]] = i

    def twoSumTP(self, nums, target):
        l = 0
        r = len(nums) - 1
        while r > l:
            if nums[l]+nums[r] == target:
                return [l, r]
            r-=1
            if r==l:
                l+=1
                r = len(nums)-1




s = Solution()
nums = [1,2,3,4,5,6]
target = 11
print(s.twoSumTP(nums, target))