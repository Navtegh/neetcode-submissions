class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums=[]
        for i in range (0,len(tokens),1):
            if tokens[i]!='+' and tokens[i]!='-' and tokens[i]!='*' and tokens[i]!='/':
                nums.append(int(tokens[i]))
            else:
                if tokens[i]=='+':
                    x=nums.pop()+nums.pop()
                    nums.append(x)
                elif tokens[i]=='-':
                    first=nums.pop()
                    second=nums.pop()
                    x=second-first
                    nums.append(x)
                elif tokens[i]=='*':
                    x=nums.pop()*nums.pop()
                    nums.append(x)
                elif tokens[i]=='/':
                    first=nums.pop()
                    second=nums.pop()
                    x=int(second/first)
                    nums.append(x)
        return nums[-1]