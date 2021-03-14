file = open("regex_sum_1189926.txt", "r")
data = file.read()

import re

# Create a regular expression to look for numbers hidden in the file
numberRegex = re.compile(r"[0-9]+")

# Find all numbers and store in a variable
number = numberRegex.findall(data)    #or "number = re.findall("[0-9]+", data)" and skip line 7

# Convert the strings to integers and sum all intergers
num = 0
for i in number:
    num1 = int(i)
    num += num1

print("Sum: " + str(num))
print("There are "+ str(len(number)) + " values.")
