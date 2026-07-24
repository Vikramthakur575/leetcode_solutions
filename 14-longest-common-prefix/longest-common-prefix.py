class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return""
        first=strs[0]

        for i in range (len(first)):
                for words in strs [1:]:

                     if i>=len(words) or words[i] != first[i]:
                        return first[:i]

        return first
        
        