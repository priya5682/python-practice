# 9\. Count Digits Write a function count_digits(n) that returns the number of digits in an integer. Example: count_digits(12345) → 5
def count_number(num):
    return len(str(abs(num)))
number = int(input("enter a number: "))
print("Length of number: ", count_number(number))