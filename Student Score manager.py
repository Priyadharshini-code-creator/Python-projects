Students=[]
print("How many Student's data you are going to upload?")
data_count=int(input())
if data_count==0:
    print("Please Enter the correct format!")
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


    