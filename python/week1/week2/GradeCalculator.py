numbergrade = int(input("Enter number grade from 1-100: "))
lettergrade = ""

if (90 <= numbergrade <=99):
    lettergrade = "A"
elif (80 <= numbergrade <= 89):
    lettergrade = "B"
elif (70 <= numbergrade <= 79):
    lettergrade = "C"
elif (60 <= numbergrade <= 69):
    lettergrade = "D"
elif (50 <= numbergrade <= 59):
    lettergrade = "F"

print("You got a " + lettergrade)