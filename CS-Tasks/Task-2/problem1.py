#1 4 5 4 4 1 2 3
#4

def sort(x):
     x.sort()
     return x    
 
    
def apperance (lst,trg):
     first= lst.index(trg) 
     last= (len(lst)-1)-(lst[::-1].index(trg))
     return first , last
 
lst=[1 ,4 ,5 ,4 ,4 ,1 ,2 ,3]    
trg=4
sort(lst)
print(apperance(lst, trg))