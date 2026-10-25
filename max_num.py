# 3\. Find the Maximum Write a function find_max(a, b, c) that returns the largest of three numbers without using max().
def max_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a = float(input("enter a number: "))
b = float(input("enter a number: "))
c = float(input("enter a number: "))
print("largest number is: ", max_num(a,b,c))