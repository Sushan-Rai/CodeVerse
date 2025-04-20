class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        x = map(str,path.split("/"))
        stack = []
        res = ""
        i = 0
        print(x)
        while i < len(x):
            print(x[i])
            if x[i] == '..':
                if stack:
                    stack.pop()
            elif x[i] == '.'  or x[i] =='':
                i+=1
                continue
            else:
                stack.append(str(x[i]))
            i+=1
        print(stack)
        for i in stack:
            if i != '' or i != '.':
                res= res + "/" + i
        if res == '':
            res = '/'
        return res