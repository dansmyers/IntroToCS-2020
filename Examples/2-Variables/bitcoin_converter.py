"""
Convert Bitcoins to USD

Goal: show off input and formatted printing
"""

# Read some number of bitcoins from the terminal
bitcoins = input('Enter a number of bitcoins: ')

# The value returned by input is always a string type (str)
# The float function turns that string into a number so we can do math on it
# In this case, the converted is saved back into the variable named bitcoins
bitcoins = float(bitcoins)

# Convert bitcoins to dollars using the conversion factor
usd = bitcoins * 8934.61

# Print to two decimal places
# %.2f is what Python calls a "format specifier"

# When you print a string that contains a format specifier, Python looks for a variable
# that comes after the string
#
# Python substitutes the variable's value into the string and formats it according
# to the format specifier

# In this case, %.2f tells Python to print only two digits after the decimal place
print('That is %.1f U.S. dollars.' % usd)
