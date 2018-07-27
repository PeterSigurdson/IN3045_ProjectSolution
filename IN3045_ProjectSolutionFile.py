# QUESTION 1
# print the result of dividing two numbers. (HINT: / is the division operator)

a = 11

b =3

print(a/b)

#QUESTION 2
#Write a PYTHON program to swap two numbers.

a = 7
b = 4

print(a,b)

c = a
a = b
b = c

print(a,b)

# Q3
# Write a PYTHON program to print the output of multiplication of three numbers which will be entered by the user.

a = input("Please enter a number:    ")
b = input("Please enter a number:    ")
c = input("Please enter a number:    ")
result = int(a) * int(b) * int(c)

print(" result: ", result)

# Q4
# Write a PYTHON program that takes a number as input and print its multiplication table.  X1 to X10

a = input("give me a Number!!!  ")

for x in range(1,11):
    print(x, " times ", a , " is ", int(x) * int(a))

# Q5
# Write a PYTHON program that takes four numbers as input to calculate and print the average. 

a = input("give me a Number!!!  ")
b = input("give me a Number!!!  ")
c = input("give me a Number!!!  ")
d = input("give me a Number!!!  ")

sum = int(a) + int(b) + int(c) + int(d)
print("sum is ", sum)

average = sum / 4

print(average)


# Q6
# Write a PYTHON program that takes an age (for example 20) as input and prints something as "You look older than 20".

gender = input("Are you a guy or a girl? (type male or female)  ")

if gender == 'female':
    print('you sure look cute!!!!')
    
else:

    age = input("what is your age?")
    
    print("you sure look older than ", age, " !!! ")

# Q7
# Write a PYTHON program to compute the sum of two given integers, if two values are equal then return the triple of their sum.

a = input("Give me a Number!!!   ")
b = input("another number:   ")

if a==b:
    print(3*(int(a) * int(b)))
    
else:
    print("those are NICE NUMBERS!!!")

# Q8
# Write a PYTHON program to check if a given integer is within 20 of 100

a = input("Give me a Number!!!   ")

if ( (100-int(a) >79) or (int(a)-100) < 121):
    print("yeah!!!")
    
else: 
    print("NNOOO!!!")
    
    