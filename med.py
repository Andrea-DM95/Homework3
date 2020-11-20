def med(A,k):
    A.sort()
    return A[k-1]
    
f=open("rosalind_med.txt","r")
n=int(f.readline())
A=list(map(int,f.readline().split()))
k=int(f.readline())
f.close()
r=med(A,k)
nf=open("output_med.txt","w")
nf.write(str(r))
nf.close()
