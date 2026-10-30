"""Ross Gallagher
banner ID:B01886848
date: 9/6/2024"""

import math

def main(): 
    num = int(input("enter a number: "))

    print(f"Times table for {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


main()