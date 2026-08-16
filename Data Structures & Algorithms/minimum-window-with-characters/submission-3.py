class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        hashmap = {}

        for ch in t:
            if ch in hashmap:
                hashmap[ch] += 1
            else:
                hashmap[ch] = 1

        window = {}

        have = 0
        need = len(hashmap)

        l = 0
        r = 0

        min_len = float("inf")
        ans = ""

        while r < len(s):

            c = s[r]

            if c in window:
                window[c] += 1
            else:
                window[c] = 1

            if c in hashmap:

                if window[c] == hashmap[c]:
                    have += 1

            while have == need:

                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    ans = s[l:r+1]

                left = s[l]

                window[left] -= 1

                if left in hashmap:

                    if window[left] < hashmap[left]:
                        have -= 1

                l += 1

            r += 1

        return ans