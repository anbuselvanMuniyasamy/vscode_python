#  # 5. REVERSE A NUMBER (SLICING)

# num = int(input("Enter the Number : "))
# rev = int(str(num)[::-1])
# print(" REVERSED NUMBER IS : ",rev)

#  # USING LOGIC
 
# num = int(input("Enter the Number : "))
# rev = 0
# while(num > 0):
#     dig = num % 10
#     rev = rev * 10 + dig
#     num = num // 10
# print(" THE REVERSED NUMBER IS : ", rev)

#  # USING RECURSIVE FUNCTION

# def reverse(string):
#     if len(string) == 0:
#         return string
#     else:
#         return reverse(string[1:]) + string[0]
# a = str(input("Enter the string to be reversed: "))
# print(reverse(a))


#  # improved recursive using math
# num = int(input("Enter the Number: "))
# def rev_num_math(num, rev=0):
#     if num == 0:
#         return rev
#     else:
#        return rev_num_math(num // 10, rev * 10 + num % 10)
# reversed_number = rev_num_math(num)
# print("Reversed Number:", reversed_number)



        
    
