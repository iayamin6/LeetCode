class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i=0
        j=len(nums)-1
        li=[]

        for c in range(len(nums)):
            li.append(tuple([nums[c],c]))
        

        sorted_arr=sorted(li)

        while j>i:

            summation = sorted_arr[i][0] + sorted_arr[j][0] 
            if  summation == target:
                if sorted_arr[i][1] > sorted_arr[j][1]:
                    return [sorted_arr[j][1], sorted_arr[i][1]]
                
                return [sorted_arr[i][1], sorted_arr[j][1]]


            else: 
                if summation > target:
                    j-=1
                else:
                    i+=1

        
        return False