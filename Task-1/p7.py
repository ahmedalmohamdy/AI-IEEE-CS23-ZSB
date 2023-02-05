def rotate_list(nums,y):
    n=len(nums)
    y=y%n
    ans=[0]*n
    x=n-y
    for i in range(y):
        ans[i]=nums[x]
        x+=1

    x=y
    for i in range(n-y):
        ans[x]=nums[i]
        x+=1
    return ans
nums=[int(num) for num in input("Enter the list numbers : ").split()]
y=int(input())
ans=rotate_list(nums,y)
print(*ans, sep = " ")