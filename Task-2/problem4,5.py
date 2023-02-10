info={}
with open(r"C:\Users\HP\Desktop\AI tasks and nots\task2\grades.txt") as myfile:
    usr_data=myfile.readline().split()
    x=[usr_data[0],usr_data[1],usr_data[4]]
    info={
        int(line.split()[0]):
        {
            usr_data[1]:line.split()[1],      
            usr_data[2]:int(line.split()[2]), 
            usr_data[4]:int(line.split()[4]), 
            usr_data[6]:line.split()[6]       
        }
        for line in myfile.readlines() if line.split()[2]!='N/A' 
          } 
        
print(info)        
#question1
oldest= min([value["birthyear"] for value in info.values()])
Oldest_id= list(filter(lambda x: info[x]["birthyear"] == oldest, info.keys()))[0]
print(Oldest_id)
#question2
su_m=sum([usr_data['grade'] for usr_data in info.values()])
avg=su_m/len(info.keys())
print(avg)

#question3
max_score=max([usr_data['grade'] for usr_data in info.values()])
gender_of_max_score= list(filter(lambda x: info[x]["grade"] == max_score, info.keys()))[0]
print(info[gender_of_max_score]['gender'])

#problem5
with open(r"C:\Users\HP\Desktop\AI tasks and nots\task2\filtered.txt","w") as myfile:
    myfile.write(x[0]+" "+x[1]+" "+x[2]+"\n")
    for key,value in info.items():
        myfile.write("{} {} {}\n".format(key,value['name'],value['birthyear']))