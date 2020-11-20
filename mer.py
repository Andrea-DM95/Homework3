def mer(n,A,m,B):
    c=[]
    i=0
    j=0
    while i<n and j<m:
        if A[i]<B[j]:
            c.append(A[i])
            i+=1
        elif A[i]>B[j]:
            c.append(B[j])
            j+=1
        else:
            c.append(A[i])
            i+=1
    while i<n:
        c.append(A[i])
        i+=1
    while j<m:
        c.append(B[j])
        j+=1
    return c
f=open("rosalind_mer.txt","r")
n=int(f.readline())
A=list(map(int,f.readline().split()))
m=int(f.readline())
B=list(map(int,f.readline().split()))
f.close()
C=mer(n,A,m,B)
nf=open("output_mer.txt","w")
nf.write(" ".join(str(c) for c in C))
nf.close()
