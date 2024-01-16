user = "charles"
password = "admin123"

def login():
    print("Enter User & Password")

def logged_in():
    print("You are Logged in")
    quit()

while True:
    entry1 = input("User Name: ")
    entry2 = input("Password: ")

    if entry1 == user and entry2 == password:
        print("Login Successful")
        logged_in()
    else:
        print("Login Failed")
