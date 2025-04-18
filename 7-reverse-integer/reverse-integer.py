class Solution(object):
    def reverse(self, n):
        negative = n < 0
        num = abs(n)
        demo = 0

        while num> 0:
            demo = demo * 10 + num % 10
            num = num // 10

        if demo > 2 **31-1:
                return 0
        
        return - demo if negative else demo
