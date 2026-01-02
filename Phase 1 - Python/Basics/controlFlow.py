'''
Control flow in Python:
1. if-else statement
2. elif statement
3. nested if statement
'''
#1. if-else statement
'''
Syntax:
if(condition):
    Body
else:
    Body
'''
#Example
age = int(input("Enter Your Age to check vote eligibility: "))
if(age>=18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#2. elif statement
'''
Syntax:
if(condition):
    #body
elif(condition):
    #body
elif(condition):
    #body
.......
.......
else:
    #body
'''
#Example - Determine if the number is positive, negative or 0

print("Check if the number is positive,negative or zero!")
a=int(input("Enter any number: "))
if(a>0):
    print(a,"is positive number")
elif(a<0):
    print(a,"is negative number")
else:
    print(a,"is zero")
print("Operation Completed")

#3. nested if statement - one loop inside another loop
"""
Syntax:
if(condition):
    #body
elif(condition):
    if(condition):
        #body
    else(cond):
else:
    #body
"""
#Example:
num=15
if(num<0):
    print("Number is Negative")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
