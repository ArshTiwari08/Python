
class Solution:
    def twoSum(self, nums, target):
        mp = {}
        for i in range(len(nums)):
            remaining  = target - nums[i]
            if remaining in mp:
                return[mp[remaining],i]
            mp[nums[i]] =i
        return


nums = [1, 2, 3, 5, 6, 7, 3]
target = 11

obj = Solution()
print(obj.twoSum(nums,target))