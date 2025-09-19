from string import ascii_lowercase

def is_pangram(s):
    return set(ascii_lowercase).issubset(set(s.lower()))

text = input("Enter a string: ")
if is_pangram(text):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
