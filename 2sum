def two_sum_again(a):
    #create dictionary with key number, value index
    num=OrderedDict()
    for i,x in enumerate(a):
        if x in num:
            num[x].append(i)
        else:
            num[x]=[i]
    
    #confront keys to search opposite
    s=list(list())
    zero=list()
    keys=list(num.keys())
    for i in range(0,len(keys)-1):
        for j in range(i+1,len(keys)):
            if keys[i]==-1*keys[j]:
                k1=(num[keys[i]])[0]
                for k2 in num[keys[j]]:
                    if k1<k2:
                        s.append([k1+1,k2+1])
    #handle 0 case
        if keys[i]==0:
            for ind in num[keys[i]]:
                zero.append(ind+1)
    
    if len(s)>=1:
        if len(zero)>1:
            if s[0][0]>zero[0]:
                return "{} {}".format(zero[0],zero[1])
            else: 
                return "{} {}".format(*s[0])
        else:
            return "{} {}".format(*s[0])
 
    elif len(zero)>1:
         return "{} {}".format(zero[0],zero[1])
    else:
        return "-1"

#two_sum AGAIN
f=open("rosalind_2sum.txt","r")
k,n=map(int,f.readline().split())
result=[]
for _ in range(k):
    a=list(map(int,f.readline().split()))
    result.append(two_sum_again(a))
f.close()
nf=open("output_2sum_again.txt","w")
nf.write("\n".join(str(r) for r in result))
nf.close()
