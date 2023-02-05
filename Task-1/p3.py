dict1 = {
    "A":[20,30,100,49],
    "B":[00,199,201,29],
    "C":[40,90,69,18]
}
x=dict1["A"]
y=dict1["B"]
z=dict1["C"]
r1= max(x)-min(x)
r2= max(y)-min(y)
r3= max(z)-min(z)
m=max([r1,r2,r3])
if m ==r1:
    print("A")
elif m==r2:
    print("B")
elif m==r3:
    print("C")