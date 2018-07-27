# Q4
# Write a PYTHON program that takes a number as input and print its multiplication table.  X1 to X10

a = input("give me a Number!!!  ")

for x in range(1,11):
    print(x, " times ", a , " is ", int(x) * int(a))