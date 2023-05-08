x = input().split(",")
list =[]
for i in x :
    list.append(i.split(":"))

x = input().split(",")
for i in x :
    list.append(i.split(":"))

list = dict(list)
dict = {}
for key , value in list.items() :
    dict.setdefault(key,int(value)) 

print(dict)