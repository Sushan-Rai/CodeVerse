class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        sum = 0
        while i < len(s):
            if s[i] == "I":
                sum+=1
                i+=1
                if i < len(s):
                    if s[i] == "V":
                        sum+=3
                    elif s[i] == "X":
                        sum+=8
                    else:
                        i-=1
                else:
                    i-=1
            elif s[i] == "X":
                sum+=10
                i+=1
                if i < len(s):
                    if s[i] == "L":
                        sum+=30
                    elif s[i] == "C":
                        sum+=80
                    else:
                        i-=1
                else:
                    i-=1
            elif s[i] == "C":
                sum+=100
                i+=1
                if i < len(s):
                    if s[i] == "D":
                        sum+=300
                    elif s[i] == "M":
                        sum+=800
                    else:
                        i-=1
                else:
                    i-=1
            elif s[i] == "V":
                sum+=5
            elif s[i] == "L":
                sum+=50
            elif s[i] == "D":
                sum+=500
            elif s[i] == "M":
                sum+=1000
            i+=1
        return sum
            
                