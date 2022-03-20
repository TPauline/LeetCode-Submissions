class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        for i in range(len(nums)):
            if not (i > 0 and nums[i] == nums[i-1]):  
                j = i+1
                k = len(nums)-1
                while j < len(nums) and k > j:

                    if nums[i]+nums[j]+nums[k] < 0:
                        j+=1
                    elif nums[i]+nums[j]+nums[k] > 0:
                        k-=1
                    else:
                        print([nums[i],nums[j],nums[k]])
                        res.append([nums[i],nums[j],nums[k]])

                        j+=1
                        while nums[j] == nums[j-1] and j < k:
                            j+=1
        
            
        return res
                    
