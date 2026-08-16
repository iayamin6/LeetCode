class Solution:
    def isValid(self, s: str) -> bool:
        

            stack= {')':'(' , '}': '{', ']': '[' }
            st=[]

            for i in s:
                if i=="(" or i== '{' or i== '[':
                    st.append(i)
            
                else:
                    if len(st)==0:
                        return False

                    if st[-1] == stack[i]:
                        st.pop()
                    else:
                        return False


                    
            if len(st)==0:
                    return True
            else:
                    return False
