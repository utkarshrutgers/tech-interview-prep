"""Solution1 without converting string"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0 or (x!=0 and x%10 ==0)):
            return False
        
        
        rev = 0
        while(x>rev):
            rev = rev*10+ x%10
            x=int(x/10)
            
        return (x==rev or x==int(rev/10))
 
 """Solution by converting to string"""
 class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev = s[::-1]
        if(s==rev):
            return True
        else:
            return False
 
 
