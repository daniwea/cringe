import sys
from tinydb import TinyDB, Query

db = TinyDB(r'INSERT DB PATH!!!')
User = Query()

def success():
    sys.exit()


def register():
    global x
    global y
    print("username:")
    x = input()
    print("password:")
    y = input()
    db.insert({'username': x, 'password': y})
    return


def login():
    print("username:")
    x = input()
    print("password:")
    y = input()
    if bool(db.search((User.username == x) & (User.password == y))):
        print("successfully logged in")
        success()
    else:
        print("login failed")
        return

def main():
    logged = 0
    while (logged == 0):
        print(" L to log in / R to register")
        key = input()
        if key == "R":
            register()


        elif key == "L":
            login()
        else:
            print("wrong input")


if __name__ == "__main__":
    main()