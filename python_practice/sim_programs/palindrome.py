# 4) PALINDROME USING BUILT IN FUNCTION ( STRING AND NUMBERS USE INT BEFORE RUN )

# name = input("Enter the string : ")
# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]
# if is_palindrome(name):
#     print("This is a palindrome.")
# else:
#     print("It's not a palindrome.") 

    

#     # USING CONDITIONS NUMBERS ONLY

# num = input("Enter : ")  # IF USE INT , IT WILL GET ERROR ==> TypeError: 'int' object is not subscriptable
# if num == num[::-1]:
#     print("It's a palindrome!")
# else:
#     print(" It is not a palindrome!")

   # USING LOOPS WITH LOGIC

# number = int(input("Enter the Number : "))
# temp = number
# rev = 0

# while number > 0:
#     dig = number % 10
#     rev = rev*10 + dig
#     number = number // 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

   # USING RECURSION FUNCTION

n = int(input("Enter number:"))

def is_palindrome(n, temp, rev=0):
    if n == 0:  # Base case: all digits have been processed
        if temp == rev:
            return "The number is a palindrome!"
        else:
            return "The number isn't a palindrome!"
    else:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
        return is_palindrome(n, temp, rev)

result = is_palindrome(n, n)
print(result)







