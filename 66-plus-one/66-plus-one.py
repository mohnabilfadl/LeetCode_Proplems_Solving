class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        result = [int(i) for i in str(int(''.join(map(str, digits)))+1)]

        return result