class Solution(object):
    def isPalindrome(self, x):
        temp = x
        result = 0
        if (x < 0):
            return False
        while x > 0:
            result = result * 10
            result += (x % 10)
            x = x // 10
        if temp == result:
            return True
        else:
            return False
