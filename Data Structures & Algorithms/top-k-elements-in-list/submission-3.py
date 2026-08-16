class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        li=[]
        for j in range(len(nums)+1):
            li.append([])
        dic={}
        
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        for key,val in dic.items():
            li[val].append(key)

        
        count=0
        res=[]
        for s in range(len(li)-1,0,-1):
            if li[s]!=[]:
                for t in li[s]:
                    res.append(t)
                    count+=1
                    if count==k:
                        return res 
