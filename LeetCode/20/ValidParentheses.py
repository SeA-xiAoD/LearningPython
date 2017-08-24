class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(0, len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.insert(0, s[i])
            else:
                if len(stack)==0:
                    return False
                if stack[0]=='(' and s[i]==')':
                    stack.pop(0)
                elif stack[0]=='[' and s[i]==']':
                    stack.pop(0)
                elif stack[0]=='{' and s[i]=='}':
                    stack.pop(0)
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
