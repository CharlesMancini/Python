people = {"charles" : "mancini" ,"John" : "Doe"}

def intro():
    print("Welcome to the Database")
    print("To access database, enter your password")
    enter_password()
    
def enter_password():
    password = "123abc"
    entry1 = input("Enter password: ")
    if (len(entry1)<3 and (entry1!=password)):
        print("Incorrect password")
        enter_password()
    else:
        print("Access Granted")
        data_base()
        
def data_base():
    x = int(input("Clear(1), Update(2), Print(3)"))
    if x == 1:
        people.clear()
        print(people)
        print("Database Cleared")
    elif x == 2:
        update_dictionary()
    elif x == 3:
        print(people)
        print("Database Printed")
    else:
        print("Invalid input")
        data_base()
        
def update_dictionary():
    for i in range(3):
        name = input("Enter name: ")
        job = input("Enter job: ")
        people[name] = job
        print(people)
        
intro()
        
    
