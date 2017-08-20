class Solution(object):
    def reverse(self,x):
        temp = 0
        x_temp = abs(x)
        while(x_temp != 0):
            temp = temp*10 + x_temp%10
            x_temp //= 10
        if(x > 0 and temp <= 2**31-1):
            ri = temp
        elif(x < 0 and temp <= 2**31):
            ri = -temp
        else:
            ri = 0
        return ri
