income = []

#Start program
print("Welcome to Budget Calculator")

def inc():
  valid = False
  print("Let's start with your income")
  while not valid:
    
    time_period = int(input("Is your income 1. Weekly, 2. Biweekly, 3. Monthly, 4. Quaterly, 5. One off item? ")) # User protection!
    income_amount = int(input("What is your income? ")) # numcheck function needed
    income_name = input('Where is this income from? ')
    income.append([income_name, income_amount, time_period])
    print(income) # for debugging
    more_income = str(input("Do you have anymore income to add? ")).lower() # needsa to do something
    if more_income == 'n' or more_income == 'no':
      valid = True

# MAIN ROUTINE
inc()

# TODO
# loop add more income (while)
# display income to user
# expenses input - prime array with suggested expenses, and display this to the user before asking
# loop expenses
# display totals to user + array in table (tabulate!)
# allow for editing
# 
# Saving and writing to file
# Testing and debugging, trialing
# Think in terms of functions!! Define functions, and call them.




