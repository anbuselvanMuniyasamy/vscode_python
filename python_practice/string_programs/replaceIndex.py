
    # Python Program to Replace All Occurrences of ‘a’ with $ in a String

# string = input("Enter string:")

# modified_string = string.lower().replace('a', '$')

# print(f"Modified string : {modified_string}" )

#     # other method

# def replace_a(s):
#     if s == "":
#         return ""
#     first_char = '$' if s[0] == 'a' or s[0] == 'A' else s[0]
#     return first_char + replace_a(s[1:])

# string = input("Enter string: ")
# result = replace_a(string)
# print(f"Modified string: {result}")

  # how many words and letters

string = input("Enter string: ")

char = 0
word = 1

for i in string:
    char += 1
    if i == ' ':
        word += 1

print("Number of words in the string:", word)
print("Number of characters in the string:", char)



