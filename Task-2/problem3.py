#lst=[5, 4, -1, 7, 8]
lst=list(input().split())
pos=[]
neg=[]
for i in lst:
    if int(i)<0:
        neg.append(int(i))
    else:
        pos.append(int(i))
        
big_sum=sum(pos)
x=min(pos)
neg.append(x)
small_sum=sum(neg)
print(f"{pos} ({big_sum})\n{neg} ({small_sum})")  