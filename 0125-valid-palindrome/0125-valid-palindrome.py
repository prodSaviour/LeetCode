class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters_only = ""
        for char in s:
            if char.isalnum():
                letters_only += char
        if (letters_only.lower()==letters_only[::-1].lower()):
            return True
        else:
            return False