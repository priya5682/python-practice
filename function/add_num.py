# 1\. Add Two Numbers Write a function add(a, b) that returns the sum of two numbers.

def add_num(a,b):
    return a+b

a = int(input("enter first number: "))
b = int(input("enter second number: "))

print("sum of number: ", add_num(a,b))