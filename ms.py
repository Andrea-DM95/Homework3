def ms(ls):
    if len(ls) == 1:
        return ls
    left = ls[0: len(ls) // 2]
    right = ls[len(ls) // 2:]
    left = ms(left)
    right = ms(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while len(left) > 0:
        result.append(left.pop(0))
    while len(right) > 0:
        result.append(right.pop(0))
    return result
    
f=open("rosalind_ms.txt","r")
n=int(f.readline())
A=list(map(int,f.readline().split()))
f.close()
R=ms(A)
nf=open("output_ms.txt","w")
nf.write(" ".join(str(r) for r in R))
nf.close()
