# Script that checks in to Southwest automatically.  Requires 3 arguments: Confirmation Number, First Name, Last Name
# Example: SouthwestMain.py 3HJD78 David Chau

from pageObjects import HomePage
import sys

# Takes command line arguments for text fields
confirmationNumber = sys.argv[1]
firstName = sys.argv[2]
lastName = sys.argv[3]

HomePage = HomePage.HomePageObjects()

HomePage.CheckInBtn().click() # Clicks on Check In Button

# Turning Confirmation Number into a list because website won't take a string
listConfNumber = []
for letter in confirmationNumber:
    listConfNumber.append(letter)
print(listConfNumber)

for a in listConfNumber:
    HomePage.ConfirmationNumBox().send_keys(a) # Clicks on Confirmation Number box and iterates through list to type in Confirmation Number

HomePage.FirstNameBox().send_keys(firstName) # Clicks on First Name box and types in First Name

HomePage.LastNameBox().send_keys(lastName) # Clicks on Last Name box and types in Last Name

HomePage.CheckInSubmit().click() # Clicks on Check in button


