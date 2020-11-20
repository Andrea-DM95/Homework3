def ins(n,a):
    count=0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
            a[j+1] = key
            count+=1
    print(count)
f=open("rosalind_ins.txt","r")
n=int(f.readline())
a=list(map(int,f.readline().split()))
f.close()
ins(n,a)
