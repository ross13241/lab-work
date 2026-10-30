"""
name: Ross 
date: 02/10/26
banner ID:B01886848
 """

def main():
    num = int(input("Enter a number: "))
    while num>100 or num<1:
        print ("error")
        num = int(input("Enter a number: "))
    print ("your number is: ", num)

main()
