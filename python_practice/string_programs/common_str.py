
#       # Python Program to Find Common Characters in Two Strings ==> common letters
# s1=input("Enter first string:")
# s2=input("Enter second string:")
# a=list(set(s1)&set(s2))
# print("The common letters are:")
# for i in a:
#     print(i)


   # not common in two strings
s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)^set(s2))
print("The letters are:")
for i in a:
    print(i)