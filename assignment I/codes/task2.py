#Create a program that takes a list of student names and stores them in a file. Then, read the file and display the contents.

num=int(input("enter the number of students"))

with open("student.txt","w") as f:
 for i in range(num):
    Name= str(input("enter the student name"))
    f.write(Name)
    
print("/n Student name lists")
with open ("student.txt",'r') as f:
    for row in f:
        print(row)
        