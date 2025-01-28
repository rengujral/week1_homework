# Get user input
# The input() function displays a message to the user and waits for them to type a value.
# The typed value is stored as a string in the variable 'var'.
var = input("Please enter a value:")

# Print the value in uppercase
# The upper() method converts all alphabetic characters in the string to uppercase.
print("Upper case:", var.upper())

# Print the number of characters
# The len() function returns the total number of characters in the string
print("Number of characters:", len(var))

# Check if the input contains numeric characters
# The isdecimal() method checks if the string consists solely of numeric characters (0-9).
print("Contains numeric characters:", var.isdecimal())

# the code runs by typing in a value in the python console