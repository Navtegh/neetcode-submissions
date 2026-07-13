class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="[" or i=="(" or i=="{":
                stack.append(i)
            elif i== "]":
                if len(stack)==0:
                    return False
                x=stack.pop()
                if x!="[":
                    return False
            elif i== "}":
                if len(stack)==0:
                    return False
                x=stack.pop()
                if x!="{":
                    return False
            elif i== ")":
                if len(stack)==0:
                    return False
                x=stack.pop()
                if x!="(":
                    return False
        if len(stack)!=0:
            return False
        else:
            return True