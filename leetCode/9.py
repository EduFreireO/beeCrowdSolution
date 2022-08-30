
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        invert = [x[a] for a in range(len(x) - 1, -1, -1)]
        return ''.join(x) == ''.join(invert)