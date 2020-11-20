def par_three(A):
    l=[]
    r=[]
    e=[]
    key=A.pop(0)
    e.append(key)
    for element in A:
        if element<key:
            l.append(element)
        elif element>key:
            r.append(element)
        else:
            e.append(element)
    return l+e+r
    
f=open("rosalind_par3.txt","r")
n=int(f.readline())
A=list(map(int,f.readline().split()))
f.close()
R=par_three(A)
nf=open("output_par3.txt","w")
nf.write(" ".join(str(r) for r in R))
nf.close()
