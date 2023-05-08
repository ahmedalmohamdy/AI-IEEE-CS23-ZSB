"""
1. Write a program (with at least 3 functions) that takes
 a list from the user and gets the measures of the spread.
 [min, Q1, Q2, Q3, max], 
 [range, IQR], [Variance, Standard deviation]-----9 8 7 10 9 1 4
"""
def fun_1(lst):
    lst.sort()
    mi_n=lst[0]
    ma_x=lst[-1]
    if len(lst)%2==0:
        q2=(lst[int(len(lst)/2)]+lst[int(len(lst)/2-1)])/2
        if (len(lst)/2)%2==0:
            q1=(lst[int(len(lst)/4)]+lst[int((len(lst)/4)-1)])/2
            q3=(lst[int(len(lst)*(3/4))]+lst[int((len(lst)*(3/4))-1)])/2
        else:
            q1=lst[int((len(lst)-2)/4)]
            q3=lst[int(((3/4)*len(lst))-.5)]
            
    else:
        q2=lst[int((len(lst)-1)/2)]
        if ((len(lst)+1)/2)%2 !=0:
         q1=(lst[int((len(lst)-1)/4)] + lst[int((len(lst)-5)/4)])/2
         q3=(lst[int((3*len(lst)-3)/4)] + lst[int((3*len(lst)+1)/4)])/2
        else:
         q1=lst[int((len(lst)-3)/4)]
         q3=lst[int((3*len(lst)-1)/4)]
    return q3,q1,q2,mi_n,ma_x

def fun_2(lst):
    lst.sort()
    rang_e=lst[-1]-lst[0]
    q3,q1,_,_,_ = fun_1(lst)
    iqr=q3-q1
    print(f"range: {rang_e}\nIQR: {iqr}")
    
def fun_3(lst):
    mean=sum(lst)/len(lst)
    variance_lst=[]
    for i in lst:
        v=(i-mean)**2
        variance_lst.append(v)
    variance=round(sum(variance_lst)/len(variance_lst),3)
    Standard_diviation=round(variance**(1/2),3)
    print(f"Variance: {variance}\nStandard deviation: {Standard_diviation}")


try:
 x=list(input("enter the list numbers here : ").split())
 lst=list(map(float,x))
 q3,q1,q2,mi_n,ma_x=fun_1(lst)
 print(f"min: {mi_n}\nQ1: {q1}\nQ2: {q2}\nQ3: {q3}\nmax: {ma_x}")    
 fun_2(lst)
 fun_3(lst)
except ValueError:
    print("please enter only number my dear")
except KeyboardInterrupt:
    print("you exit program")
    
except:
    print("something went wrong try again and make sure you enter more than 3 numbers ")
          
finally:
    print("Program's ENd THANKS ")


#I DON'T USE ANY library      KINDLY deserve bouns?











