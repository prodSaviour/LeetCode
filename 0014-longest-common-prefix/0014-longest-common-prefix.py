class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short=min(strs, key=len)
        for i in strs:
            i=i[:len(short)]
            if (i==short):
                continue
            else:
                while (short!=i):
                    short=short[:-1]
                    i=i[:len(short)]
        return short