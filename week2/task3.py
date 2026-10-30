"""
name: Ross 
date: 02/10/26
banner ID:B01886848
 """

def main():
    
    eggs = int(input("Enter the number of eggs: "))

    # 144 eggs in a gross
    grossegg = 144

    # 12 eggs in a dozen
    dozenegg = 12

    # Calculate how many complete grosses there are
    gross = eggs // grossegg

    # Calculate how many eggs are left after taking out the grosses
    remainingeggs = eggs % grossegg

    # Calculate how many complete dozens are in the remaining eggs
    dozen = remainingeggs // dozenegg

    # Calculate how many individual eggs are left
    eggs_left = remainingeggs % dozenegg

    
    print(gross, "gross")
    print(dozen, "dozen")
    print(eggs_left, "eggs left")


# Start the program
main()
