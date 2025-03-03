class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Convert number to string and check if it reads the same backward.
        """
        return str(x) == str(x)[::-1]
