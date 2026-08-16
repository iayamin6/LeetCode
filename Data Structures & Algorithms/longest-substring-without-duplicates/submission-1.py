class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            left = 0
            right = 0
            max_len = 0
            st = set()

            while right < len(s):

                while s[right] in st:
                    st.remove(s[left])
                    left += 1

                st.add(s[right])

                length = right - left + 1
                max_len = max(max_len, length)

                right += 1

            return max_len