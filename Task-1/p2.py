x=[1,2,3,4,3,2,1]  # is symmetric
f =True
for i in range(len(x)):
    
    if x[i]==x[-i-1]:
       f=True
       i+=1 
    else :
        f=False
        break
        
if f==True:
        print("is symmetric")
else :
        print("is not symmetric")