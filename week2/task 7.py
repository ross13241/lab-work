"""Ross Gallagher
banner ID:B01886848
date: 9/6/2024"""

def main():
    a = 0
    b = 1

    for i in range(20):
        print(a, end=" ")
        next_term = a + b
        a = b
        b = next_term

main()


    