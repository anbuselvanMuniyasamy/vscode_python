  # Python Program to Remove the nth Index Character from a Non-Empty String

text = input("Enter a string: ")
index = int(input("Enter the index to remove: "))

def remove_nth_char(s, n):
    return s[:n] + s[n+1:]

print("Result:", remove_nth_char(text, index))
