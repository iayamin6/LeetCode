class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        li=[]
        for i in strs:
          d=sorted(i)
          li.append(tuple([d,i]))
        strs1=sorted(li)

        li2=[]
        li3=[]

        for f in range(len(strs1)):

          if f==len(strs1)-1:
            li3.append(strs1[f][1])
            li2.append(li3)
            li3=[]

          
          elif strs1[f][0]!=strs1[f+1][0]:
              
              li3.append(strs1[f][1])
              li2.append(li3)
              li3=[]
          
          elif strs1[f][0]==strs1[f+1][0]:
            li3.append(strs1[f][1])

        
        return li2