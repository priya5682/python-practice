# 5\. Reverse a String Write a function reverse_string(s) that returns the reversed string. Example: reverse_string("python") → "nohtyp"
def reverse_string(s):
    return s[::-1]
string = input("enter a string: ")
print("reverse of string: ", reverse_string(string))