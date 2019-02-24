"""Solution 1"""
class Solution(object):
    def reverse(self, x):
        
        if (str(x)[0])=='-':
            s = str(x)[1:]
            b = '-'+s[::-1]
            if int(b)>2**31-1 or int(b)<-2**31:
                return 0
            return int(b)
        else:
            s = str(x)
            b = s[::-1]
            if int(b)>2**31-1 or int(b)<-2**31:
                return 0
            return int(b)

"""Solution2"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        ret = int(('-' if x < 0 else '') + str(abs(x))[::-1].lstrip("0"))

        if abs(ret) > (2 ** 31 - 1):
            return 0
        
        return ret
