#OPTIMIZED WITH DICTIONARY
from collections import OrderedDict
def three_sum_d (A):
    d=OrderedDict()
    for i,x in enumerate(A):
        if x in d:
            d[x].append(i)
        else:
            d[x]=[i]
        keys=list(d)
    for i in range(len(d)):
        for j in range (i, len(d)):
            tmz=(-keys[i]-keys[j])
            if tmz in d:
                for e in d[tmz]:
                    if any(e!=l for l in d[keys[i]])==True and any(e!=k for k in d[keys[j]])==True:
                        if i==j:
                            return "{} {} {}".format((d[keys[i]][0])+1,(d[keys[j]][1])+1,e+1)
                        else:
                            return "{} {} {}".format((d[keys[i]][0])+1,(d[keys[j]][0])+1,e+1)
    else:
        return "-1"

#RUN 3SUM_Dictionary
f=open("rosalind_3sum.txt","r")
k,n=map(int,f.readline().split())
result=[]
for _ in range(k):
    a=list(map(int,f.readline().split()))
    result.append(three_sum_d(a))
f.close()
nf=open("output_3sum_d.txt","w")
nf.write("\n".join(str(r) for r in result))
nf.close()
