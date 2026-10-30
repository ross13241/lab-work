"""
name: Ross 
date: 02/10/26
banner ID:B01886848
 """

import math
55
def main():
    num1 = float(input("Enter the first number: "))
    print("Your first number is: ", num1)
    num2 = float(input("Enter the second number: "))
    print("Your second number is: ", num2)

    calculate(num1, num2)


def calculate(a, b):
    print("The sum is: ", a + b)
    print("The product is: ", a * b)
    print("The first number minus the second is: ", a - b)
    print("The first number divided by the second is: ", a / b)
    print ("the second number divided by the first is: ", b / a)
    print("Integer division is: ", a // b)
    print("The modulus is: ", a % b)
    print("The first number to the power of the second is: ", a ** b)


main()

   








