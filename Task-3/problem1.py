"""
1. Write a program (with at least 3 functions) that takes a
list from the user and gets the measures
 of the center. [Mean, Median, Mode]
 9 8 7 10 9 1 4

"""
 
    
def mean(ls):
    
    mean=sum(ls)/len(ls)
    print(f"mean: {round(mean,3)}") 
    
 
def median(ls):
   lst.sort()
   if len(lst)%2 !=0:
       print(f"median: {lst[int((len(lst)-1)/2)]}")    
   else:
       print(f"median: {(ls[int((len(ls)/2))]+ls[int((len(ls)/2)-1)])/2}") 
       
def mode(ls):
   args = {}
   for i in ls:
      if i in args:
         args[i] += 1
      else:
         args[i] = 1
   print(f"mode: {max(args, key=args.get)}")   

    
try:
 x=list(input("enter : ").split())
 lst=[]
 for i in x:
    lst.append(float(i))
 mean(lst)
 median(lst)
 mode(lst)
except ValueError:
        print("You should input numbers only my dear")
except:
        print("something go wrong check your input my dear ")  