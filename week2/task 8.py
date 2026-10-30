"""
name: Ross 
date: 02/10/26
banner ID:B01886848
 """
def password():

    
    password = "ross"

    correct = 0
    incorrect = 0

    for i in range (10): #  loop 10 times to get password from user
        guess = input("enter password:") #  get password from user

        if guess == password:     # check if password is correct
            print (" passsword correct") #  get password from user and check if it is correct
            correct = correct +1 #  increment correct password count

        else:
            print ("password wrong:") #  get password from user and check if it is correct  
            incorrect = incorrect +1 #  increment incorrect password count

    percentage = (incorrect/10) * 100 # calculate percentage of incorrect password attempts

    print (f"correct password {correct}")     
    print (f"wrong password {incorrect}")
    print (f"percentage of wrong attempts {percentage}%") # if percentage of incorrect password attempts is greater than 50% print alert message

    if percentage > 50: #   if percentage of incorrect password attempts is greater than 50% print alert message
        print ("alert: more than 50% of password were incorrect")

password()

   
def password1():

    
    password = "ross"

    currect = 0
    incorrect = 0

    max_attempt = (10)
    attempt = 1
    for i in range (1, 11):
        guess = input("enter passowrd:")
        attempt = attempt + 1

        if guess == password:
            print ("password correct")
            currect = currect + 1
            break
       


    if i < (10):
        print (" access granted")

    else:
        print ("max attempts reached")



   

password1()


def  authentication():


    username = "ross"
    password = "ross"

    for i in range (1, 4):
        username = input("enter username:") # get username from user
        password = input("enterpassword:") #get password from user

        if username == "ross" and password == "ross": #get username and password from user and check if they are correct
            print ("login successful:") #get username and password from user and check if they are correct
            break
        elif  i >= 3:
    
            print ("login failed account locked for 24 hours:") #   get username and password from user and check if they are correct
            

authentication()

def exit():

        

    exit = input("do you want to leave (y/n):") # ask user if they want to leave
    if exit == "y": # if user wants to leave print goodbye message
        print ("goodbye")
    else:
        print ("welcome back") # if user does not want to leave print welcome back message

exit()




                   
           
    



