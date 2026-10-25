# 6\. Check Palindrome Write a function is_palindrome(s) that checks whether a string reads the same forward and backward. Example: is_palindrome("madam") → True
import string
def is_palindrome(s):
    return s[::-1]
string = input("enter a string:")
print("Palindrome string is: ", is_palindrome(string))