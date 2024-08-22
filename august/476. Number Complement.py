***************************** 476. Number Complement  ****************************************************************************************
 Approach I 
 
# Python Code 

class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)  # a= 0b101
        b = str(a[2:]) # a= 0b101 --> b= "101"
        r = []
        for i in b:
            if i=='0':
                r.append('1')  # 0->1
            else:
                r.append('0')  # 1-> 0
       # r= ['0,'1','0']
        c=''.join(r)         # r= ['0,'1','0'] -> 010
        e = str(c)  # 010 --> "010"
        f = int(e,2)  # "010" --> 2
        return f

///////////////        Approach II          ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Solution:
    def findComplement(self, num: int) -> int:
       bit_length = num.bit_length()  # num = 5  bit length = 3
       
       mask = (1 << bit_length) - 1   # (1 << 3 ) - 1 -> 1000 - 1 --> 111 {7} 

       return num ^ mask  # 5 ^ 7 -> 2
