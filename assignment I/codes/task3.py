# Implement a program to store student records (name, roll, marks,contact number) using a dictionary.
# a. Provide menu options to add, search, and display students.

Student_records = []
loop = True

while loop:

    user_input = input('Enter:\n 1)Add record\n 2)Search record\n 3)Dislay all records\n 4)Exit\n')

    if user_input == "1":
        name = input('Enter name: ')
        roll_no = input('Enter roll number: ')
        marks= input('Enter marks percentage: ')
        contact_num = input('Enter contact number: ')
        data = {'name': name, 'roll': roll_no, 'marks': marks, 'contact': contact_num}
        Student_records.append(data)
        print(f'Inserted data: {data}')

    elif user_input == "2":
        search = input('Enter student name to search for his/her record: ')

        for std in Student_records:
            if(std['name'] == search):
                print(f'Name: {std['name']} Roll Number: {std['roll']} Marks: {std['marks']} Contact: {std['contact']}')

    elif user_input == "3":
        for std in Student_records:
            print(f'Name: {std['name']} Roll Number: {std['roll']} Marks: {std['marks']} Contact: {std['contact']}')
    
    elif user_input == '4':
        loop = False

    else:
        print("Invalid option")