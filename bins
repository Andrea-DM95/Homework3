def bins(n,a,search):
    first=0
    last=n-1
    #recursive call
    while first<=last:
        #assign middle as middle of array
        middle=(last+first)//2
        #if search equals to middle returns position in array (not index) of element
        if a[middle]==search:
            return middle+1
        #if search is minor middle we search in first half
        elif a[middle]>search:
            last=middle-1
        #if search is bigger than middle we search in second half
        elif a[middle]<search:
            first=middle+1
    #if while ends it means search was not in array
    return -1

f=open("rosalind_bins.txt","r")
n=int(f.readline())
m=int(f.readline())
a=list(map(int,f.readline().split()))
s=list(map(int,f.readline().split()))
f.close()
result=[]
for search in s:
    result.append(bins(n,a,search))
nf=open("output_bins.txt","w")
nf.write(" ".join(str(r) for r in result))
nf.close()
