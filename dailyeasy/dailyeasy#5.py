with open("pass.txt", "r") as fo:
    user = fo.readline().strip()
    password = fo.readline().strip()


while (True):
    userInput = raw_input("Enter user name: ")
    passwordInput = raw_input("Enter password: ")
    if (userInput == user and passwordInput == password):
        print "Success"
        break
    else: print "Failure"
fo.close()
