class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
            
            dic={}
            l=0
            r=0
            max_freq=0
            max_len=0
            while r < len(s):

                if s[r] in dic:
                    dic[s[r]] += 1
                else:
                    dic[s[r]] = 1

                length = r - l + 1
                max_freq = max(dic.values())

                while length - max_freq > k:
                    dic[s[l]] -= 1
                    l += 1
                    length = r - l + 1

                max_len = max(max_len, length)
                r += 1

            return max_len