import sys
x = "default"
y = "default"

def success():
    sys.exit()

def register():
    global x
    global y
    print("username:")
    x = input()
    print("password:")
    y = input()
    return

def login():
    print("username:")
    if x == input():
        print("password:")
        if y == input():
            print("successfully logged in")
            success()
        else: print("wrong password")
    else: print("wrong username")
def main():
    logged = 0
    while(logged == 0):
        print(" L to log in / R to register")
        key = input()
        if key == "R":
            register()


        elif key == "L":
            login()
        else: print("wrong input")
if __name__ == "__main__":
    main()




