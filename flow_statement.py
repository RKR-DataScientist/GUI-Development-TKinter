# >>>>>>>>>>>>>>>>>>>.Python Flow Control Statements
# PYTHON IF STATEMENT

num = int(input("Enter any number:- "))
if num >= 1:
    print(" You have entered the positive number")

# Python If Else Statement Example
marks = int(input(" Please enter your subject marks:"))
if marks >= 50:
    print("Congratullation you got passing marks:-", (marks))
else:
    print(" You failed, Better luck next time")

# Python Nested If Example
age = int(input(" Enter your age :- "))
if age < 18:
    print(" You are under age, not eligible for job")
else:
    if age >= 18 and age < 60:
        print(" You are eligible for the job, fill the detail")
    else:
        print(" You are too OLD as per goverment job")

# Python Elif Example
# Imagine you have 6 subjects and Grand total is 600
Tmarks = int(input(" Please your total obtain marks :- "))
if marks>=540:
    print(" Congratulations! ")
    print(" You are eligible for Full Scholarship ")
elif marks >= 480:
    print(" Congratulations! ")
    print(" You are eligible for 50 Percent Scholarship ")
elif marks >= 400:
    print(" Congratulations! ")
    print(" You are eligible for 10 Percent Scholarship ")
elif marks:
    print(" You are Not eligible for Scholarship ")
    print(" We are really Sorry for You ")

# ...........Python While loop Example
total = 0
number = int(input("Enter any number :- "))
while(number <= 10):
    total = total+number
    number += 1
print(" value of total from the while loop is :-", total)

# Python While loop Else Example
while(number <= 10):
    total = total+number
    number += 1
    print(" value of total from the while loop is :-", total)
else:
    print(" Your value is greater than 10")

#.........Python For Loop Example
# Iterating over a String  
ex = 'ScificWebPythonTutorial'
for word in ex:
    print(" Letters at index {0} is ", word)
# iterate through the Countries List
countries = ['India', 'U K', 'U S A', 'Australia']
for country in countries:
    print("Countries are", country)

# Iterating over dictionary  
print("\nDictionary Iteration")     
d = dict()   
d['xyz'] = 123
d['abc'] = 345
for i in d :  
    print("% s % d" %(i, d[i]))  

#.......... Python For Loop range() function Example
# printing a number
for i in range(10):
    print(i, end=" ")
print()
# using range for iteration 
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i], end=" ")
print()

# performing sum of natural number  
sum = 0
for i in range(1, 10):
    sum = sum + i
print("Sum of first 10 natural number :", sum)    

# Python For Loop with Range number after 2
for num in range(1,20,2):
    print(" Number adding with 2:-", num)

# Python For Loop Else Example
number = int(input(" Please enter any integer below 100: "))
for i in range(0,100):
    if number == i:
        print(" User entered Value is within the Range (Below 100)")
        break
else:
    print(" User entered Value is Outside the Range (Above 100)")

# ............Python Break Statement in While Loop
i = 0
while i <= 10:
    print("The value of the variable i = ", i)
    i = i+1
    if i == 4:
        break

#...........Python Continue Statement in For Loop Example
# Python Continue Statement in For Loop example
num = int(input(" Enter any number:- "))
for i in range(1, num):
    if(i%2 !=0):
        print(" Odd number = {0}( Skipped by continue)".format(i))
        continue
    print("Even Number = ",i)

# Python Continue in While Loop Example
i = 0
while(i<=10):
    if (i == 5 or i == 9):
        print("Skipped  Number:-",i)
        i +=1
        continue
    else:
        print(" The value of index i is :- ", i)
        i +=1
