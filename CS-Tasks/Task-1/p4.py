x = list(input("List Of Number : ").split())
targ = int(input("Target Number : "))
y = x.index(str(targ))
print(f"{y-2}, {y -1}")