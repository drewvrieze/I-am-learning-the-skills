def addStudent():
    id = input("Enter the new student id: ")
    first = input("First Name: ")
    last = input("Last Name: ")
    major = input("Major: ")
    phone = input("Phone: ")
    query = f"""insert into students (id,first,last,phone,major) values ({id},'{first}','{last}','{phone}')"""
    print(query)

    pass

def deleteStudent():
    pass

def showStudent():
    print("Enter the id information for the student")
    id = input("Id: ")
    query = f""" select * from students whiere id={id}""" 
    print(query)
    pass

def updateStudent():
    id = input("Enter the student ID: ")
    first = input("First Name: ")
    last = input("Last Name: ")
    major = input("Major: ")
    phone = input("Phone: ")
    query = f"""update students set first='{first}', last = '{last}', phone = '{phone}', major = '{major}' where id = {id};"""
    
    print(query)

choice="1"
while (choice!='0'):
    print("0) Add a student")
    print("1) Delete a student")
    print("2) Show a student")
    print("3) Update a student")
    print("0) Quit")
    choice = input("Type the number for your choice: ")
    if (choice == '0'):
        addStudent()
    if (choice == '1'):
        deleteStudent()
    if (choice == '2'):
        showStudent()
    if (choice == '3'):
        updateStudent()