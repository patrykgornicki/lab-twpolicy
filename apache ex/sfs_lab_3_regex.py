# SFS Lab 3 - Python Regex Questions
# EC May, 2022
# Add your answer to each of the questions

#Patryk Gornicki ec2092516

import re


# Q1 Import the apache log and print out the contents
# your code here
file = "apache_log"
with open(file) as file:
    lines = file.readlines()
#print(lines)

# once you have answer for Q1 comment out the print statement to keep things tidy

# Q2 Use regex to find any instance of the word notice?
# your code here
for line in lines:
    x = re.findall("notice", line)
    if (x):
        print(line)

# Q3 Use regex to find any instance of the word error?
# your code here
for line in lines:
    x = re.findall("error", line)
    if (x):
        print(line)

# Q4 Use regex to count any instance of the word notice?
# your code here
count = 0
for line in lines:
    x = re.findall("notice", line)
    if (x):
        count += len(x)
print(f"Notice occured {count} times")

# Q5 Use regex to count any instance of the word error?
# your code here

count = 0
for line in lines:
    x = re.findall("error", line)
    if (x):
        count += len(x)
print(f"Error occured {count} times")
# Q6 Use regex to count any instance of the letter p?
# your code here
count = 0
for line in lines:
    x = re.findall("p", line)
    if (x):
        count += len(x)
print(f"p occured {count} times")

# Q7 Use regex to find any instance of the string jk2_init?
# your code here
for line in lines:
    x = re.findall("jk2_init", line)
    if (x):
        print(line)

# Q8 Use regex to find any appearance of the number 6754?
# your code here
for line in lines:
    x = re.findall("6754", line)
    if (x):
        print(line)

# Q9 Use regex to find any appearance of the number 6?
# your code here
for line in lines:
    x = re.findall("6", line)
    if (x):
        print(line)

# Q10 Use regex to find any ip addresses?
# your code here
for line in lines:
    x = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
    if (x):
        print(line)


# Q11 Create a script that will ask for user input, ask the user to enter a letter, then use regex to return any matches of that letter in the file?
# your code here
question = input("Type a letter:")

for line in lines:
    x = re.findall(question, line)
    if (x):
        print(line)
# Q12 adapt your answer from Q11, to use a function to search the file, the function should take one parameter - the letter you are searching for?
# your code here


def search(letter):
    for line in lines:
        x = re.findall(letter, line)
        if (x):
            print(line)
question = input("Type a letter:")
search(question)