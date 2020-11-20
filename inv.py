def inv(a):
    b=sorted(a)
    inv=0
    while len(a)>0:
        #print(len(a))
        ind=b.index(a[0])
        inv+=ind
        a.pop(0)
        b.pop(ind)
    return inv
    
f=open("rosalind_inv.txt","r")
n=int(f.readline())
A=list(map(int,f.readline().split()))
result= inv(A)
f.close()
nf=open("output_inv.txt","w")
nf.write("{}".format(result))
nf.close()

#Could be optimized further with counting swap in mergesort, but I'm still trying to understand how exactly. This is an optimization over the "brute force" method
