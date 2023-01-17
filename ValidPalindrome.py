class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for item in s.lower():
            if item.isalnum():
                new+= item
        
        return new == new[::-1]
