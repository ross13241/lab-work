"""Ross Gallagher
banner ID:B01886848
date: 9/6/2024"""


def main():

    
    password = "helloross@"

    guess = input("enter password:")

    while guess != password:
        print ("wrong password try again")
        guess = input("enter password:")

    print ("access granted")

  
main()

