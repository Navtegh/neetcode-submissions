class Solution:

    def encode(self, strs: List[str]) -> str:
        total_lists=str(len(strs))
        listlens=[str(len(strs[i])) for i in range(len(strs))]
        final=[total_lists]+listlens+strs
        print(",".join(final))
        return ",".join(final)

    def decode(self, s: str) -> List[str]:
        x = s.split(",")
        listlens = [int(i) for i in x[1:int(x[0])+1]]
        initial = len(",".join(x[:(1+int(x[0]))]))+1

        a=0
        fullsent=s[initial:]
        final=[]
        for i in listlens:
            sent=fullsent[a:a+i]
            final.append(sent)
            a=a+i+1
        return final





        
        
