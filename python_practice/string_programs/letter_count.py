#  # Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively
# string = input("Enter a string: ")
# char = input("Enter the letter to count: ")

# count = string.count(char)

# print(f"The letter '{char}' occurs {count} times in the string.")
   

#      # recursive 

# def count_letter(string, letter):
#     count = 0
#     for c in string:
#         if c == letter:
#             count += 1
#     return count

# string = input("Enter a string: ")
# letter = input("Enter the letter to count: ")

# result = count_letter(string, letter)
# print(f"The letter '{letter}' occurs {result} times in the string.")

#    # number of lowercase in string
# string=input("Enter string:")
# count=0
# for word in string:
#       if(word.islower()):
#             count=count+1
# print(f"The number of lowercase characters is : {count}")


#     # vowels count

# def count_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#     return count

# text = input("Enter a string: ")
# result = count_vowels(text)
# print("Number of vowels in the string:", result)


#   # vowels count and replacement

# def count_and_replace_vowels(string):
#     vowels = "aeiouAEIOU"
#     count = 0
#     modified_string = ""

#     for char in string:
#         if char in vowels:
#             count += 1
#             modified_string += "$"
#         else:
#             modified_string += char

#     return count, modified_string

# text = input("Enter a string: ")
# vowel_count, replaced_text = count_and_replace_vowels(text)

# print("Number of vowels in the string:", vowel_count)
# print("String after replacing vowels with '$':", replaced_text)

#    # count the number of lowercase and uppercase

# string=input("Enter string:")
# count1=0
# count2=0
# for i in string:
#       if(i.islower()):
#             count1=count1+1
#       elif(i.isupper()):
#             count2=count2+1
# print("The number of lowercase characters is:")
# print(count1)
# print("The number of uppercase characters is:")
# print(count2)

#     # count the numbers and characters

# string=input("Enter string:")
# count1=0
# count2=0
# for i in string:
#       if(i.isdigit()):
#             count1=count1+1
#       count2=count2+1
# print("The number of digits is:")
# print(count1)
# print("The number of characters is:")
# print(count2)