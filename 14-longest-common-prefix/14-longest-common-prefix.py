class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        for i, letter in enumerate(zip(*strs)):
            if len(set(letter)) > 1:
                return strs[0][:i]
         
        else:
            return min(strs)