""" 
Question

Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



"""



""" 

class Solution(object):
    def isPalindrome(self, x):

        # :type x: int
        # :rtype: bool

        temp = str(x)
        if x == temp[::-1]:
            return True
        
        return False


s1 = Solution()

n = 123

result = s1.isPalindrome(n)
print(result)


"""





class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        
        if x < 0:
            return False
        
        
        temp = x
        
        rev = 0
        
        
        while x>0:
            
            last_digit = x % 10
            
            rev = rev * 10 + last_digit
            
            x = x // 10
        
        
        if rev == temp:
            return True
        
        return False


s1 = Solution()

n = -121

result = s1.isPalindrome(n)
print(result)