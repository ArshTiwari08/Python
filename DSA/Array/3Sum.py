class Solution(object):
    def twoSum(self, nums, target,i,j, result):
        while i<j:
            if nums[i]+nums[j] > target:
                j-=1
            elif nums[i]+nums[j] < target:
                i+=1
            else:
                result.append([-target,nums[i],nums[j]])
                i+=1
                j-=1
                while i<j and nums[i] == nums[i+1]:
                    i+=1
                while i<j and nums[j] == nums[j-1]:
                    j-=1
    def threeSum(self,nums):
        result = []
        n = len(nums)
        if n<3:
            return []
        nums.sort()
        for i in range(n-2):
            if i >0 and nums[i]== nums[i-1]:
                continue
            target = -nums[i]
            self.twoSum(nums,target,i+1,n-1,result)
        return result

solution = Solution()
nums = [-1,0,1,2,-1,-4]
sol = solution.threeSum(nums)
print(sol)