from collections import Counter 
def maj(n,a):
    #check=False
    count=Counter(a)
    for key,value in count.items():
        if value>=n/2:
            #check=True
            return key
            break
    return -1
f=open("rosalind_maj.txt","r")
k,n=map(int,f.readline().split())
result=[]
for _ in range(k):
    a=list(map(int,f.readline().split()))
    result.append(maj(n,a))
f.close()
nf=open("output_maj.txt","w")
nf.write(" ".join(str(r) for r in result))
nf.close()
