lst=[]
print("#### Enter  the numbers and enter the letter 'q' to start #### \n")
i=0
while True:
    x=input(f"enter the [{i}]number : ")
    if x=="q":
        break
    else :
        lst.append(int(x))
        i+=1
    
lst.sort()
print(f"the second largest number is : {lst[-2]}")        
print(f"the second smallest number is: {lst[1]}")