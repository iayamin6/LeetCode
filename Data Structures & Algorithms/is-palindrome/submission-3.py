class Solution:
    def isPalindrome(self, s: str) -> bool:

        st=""

        for ch in s:
            if ch.isalnum():
                st+=ch.lower()

        i=0
        j=len(st)-1

        while i<=j:
            if st[i]!=st[j]:
                return False
            i+=1
            j-=1

        return True
        