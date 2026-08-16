class Solution:
    def findMin(self, nums: List[int]) -> int:
        
            def find_minimum_sorted_array(nums,left,right, mid):

                if nums[mid]> nums[right]:
                    left=mid+1
                
                elif nums[mid]< nums[right]:
                    right=mid
                
                nums=nums
                mid=(left + right) // 2
                if left==right:
                    return nums[left]
                return find_minimum_sorted_array(nums, left, right, mid)



            
            l=0
            r=len(nums)-1
            mid=round((r-l)/2)
            return (find_minimum_sorted_array(nums, l,r,mid))