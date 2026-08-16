class Solution:

    def encode(self, strs: List[str]) -> str:
        
        st=""
        for i in range(len(strs)):
            count=len(strs[i])
            st+=str(count)+'#'+str(strs[i])
        
        return st

    def decode(self, s: str) -> List[str]:


          li=[]


          j=0
          while j<len(s):

            num=""
            while s[j]!='#':
                num+=s[j]
                j+=1
            
            j=j+1
            num1= int(num)
            new=""
            count=0
                 
            while count<num1:
              new+=str(s[j])
              count+=1
              j+=1

            li.append(new)
          return li