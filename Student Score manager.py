Students=[]
while True:
    try:
        data_count=int(input("How many Student's data you are going to upload?\n"))
        if(data_count>100):
           print('You are exceeding the limit\n The limit is 100!')
        if(data_count>0 and data_count<=100):
           break
        else:
           print('please enter the correct format!')
    except:
        print("Invalid input! Please enter a whole number")
        
for i in range(data_count):
    name=input(f'\n Enter the name of Student {i+1}:')
    Score=int(input(f'\n Enter the score of Student {i+1}:'))
    if(Score>100 or Score<0):
        print("Please enter the correct value!")
        Score=int(input(f'\n Enter the score of Student {i+1}:'))
    students_details={
        "Name":name,
        "Score":Score
    }
    Students.append(students_details)
print("\nThe Students data are:")

for students_details in Students:
    print(students_details)

less_than_fifty=[]
for students_details in Students:
    if(students_details['Score']<50):
       less_than_fifty.append(students_details['Name'])
if less_than_fifty:
    print("\nThe students who Scored less than 50 are:") 
    for name in less_than_fifty:
        print(name)
        
print("\nThe Average of Students are:")
students_average=[]
for students_details in Students:
    students_average.append(students_details['Score'])
average=sum(students_average)/len(students_average)
print(average)


    