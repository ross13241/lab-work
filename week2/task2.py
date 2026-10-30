
"""
name: Ross 
date: 02/10/26
banner ID:B01886848
 """



# Get the GMT time from the user
def getin():
    GMTTIME = input("Enter the time in GMT: ")

   
    return GMTTIME


# Convert the GMT time into PST and CET
def convert(GMTTIME):

    # Split the hours and minutes at the colon
    hours, minutes = map(int, GMTTIME.split(":"))

    # Convert GMT to PST
    if hours >= 8:
        # Subtract 8 hours if the result stays within the same day
        pst_hours = hours - 8
    else:
        # Add 16 hours if subtracting 8 would go below 0
        pst_hours = hours + 16

    # Convert GMT to CET
    if hours <= 22:
        # Add 1 hour if the result stays within the same day
        cet_hours = hours + 1
    else:
        # Change to 00 if GMT is 23:00
        cet_hours = 0

    # Display the PST time
    print("PST:", pst_hours, ":", minutes)

    # Display the CET time
    print("CET:", cet_hours, ":", minutes)


GMTTIME = getin()

# Send the GMT time to the convert function
convert(GMTTIME)
