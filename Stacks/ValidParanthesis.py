class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        nums = []
        i = 0
        top = -1
        while i < len(s):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                nums.append(s[i])
                top+=1
            if len(nums) > 0:
                if s[i] == ')':
                    if '(' != nums[top]:
                        return False
                    else:
                        nums.pop(top)
                        top-=1
                elif s[i] == ']':
                    if '[' != nums[top]:
                        return False
                    else:
                        nums.pop(top)
                        top-=1
                elif s[i] == '}':
                    if '{' != nums[top]:
                        return False
                    else:
                        nums.pop(top)
                        top-=1 
            else:
                return False
            i+=1
        if len(nums) == 0:
            return True
        return False
        