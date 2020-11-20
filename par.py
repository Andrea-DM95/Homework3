from collections import deque
def par(A):
    B=deque()
    key=A.pop(0)
    B.append(key)
    for element in A:
        if element<=key:
            B.appendleft(element)
        elif element>key:
            B.append(element)
    return list(B)

f=open("rosalind_par.txt","r")
n=int(f.readline())
A=list(map(int,f.readline().split()))
f.close()
R=par(A)
nf=open("output_par.txt","w")
nf.write(" ".join(str(r) for r in R))
nf.close()
