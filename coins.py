# 1) Set variables for the value of each coin (in cents)
quarter = 25
dime = 10
nickel = 5
penny = 1

# 2) Get the amount of money in Jimmy's pocket from the user
#    Make sure you convert it a number (int) first!

print "Hey Jimmy! How many coins you have there?"
jimmysPocket = int(raw_input())

# 3) Take the amount of money in Jimmy's pocket and divide it by the value of the coin
# 	 Take the floor (trim off decimals) of the division and you are left with the amount of that coin
quartersInPocket = jimmysPocket // quarter

# 4) Update the amount of money left after taking out the previous coin
jimmysPocket = jimmysPocket - (quartersInPocket * quarter)

# 5) Repeat for each coin type
dimesInPocket = jimmysPocket // dime
jimmysPocket = jimmysPocket - dimesInPocket * dime

nickelsInPocket = jimmysPocket // nickel
jimmysPocket = jimmysPocket - nickelsInPocket * nickel

penniesInPocket = jimmysPocket // penny
jimmysPocket = jimmysPocket - penniesInPocket * penny

# 6) Print results
print "You need %s quarters, %s dimes, %s nickels, %s pennies." % (quartersInPocket, dimesInPocket, nickelsInPocket, penniesInPocket)


# ==================================================


# Test Cases- Strategy is to find the boundaries of the program. The goal of tests is to break the program as brutally as possible.

# 1) Values that demonstrate each coin working in isolation
	# Quarter = 25, 50, 75
    # Dime = 10, 20
    # Nickle = 5
    # Penny = 1, 2, 3

    # Testing them in isolation will prove that the each coin is fulfilling their specific role

# 2) Cases where the number is divisible by multiple coins
	# 25, 15, 10

    # Proves that it captures the number or large coins first before the smaller coins

# 3) A combination that will give a result for each coin type
	# 41

    # Demonstrates that the program trickel down is functioning


# Error Test Cases (don't know if we need to worry about them)
# - Strings/Characters
# - Negative numbers
# - Non-whole numbers
# - Null value


# ==================================================