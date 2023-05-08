x= list(input("enter here : ").split())
a=x[0]
b=x[1]
lst1=[a[:len(a)//2+1],b[:len(b)//2]]
lst2=[a[len(a)//2+1:],b[len(b)//2:]]
print(lst1)
print(lst2)