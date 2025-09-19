# using loop
# num = int(input("Enther the number to sum of the digits: "))
# count = 0
# while(num>0):
#     count += 1
#     num = num // 10 
# print(f"The sum of the digit is  {count}")


  # ANOTHER METHOD
# num = int(input("Enter a number: "))
# count = len(str(abs(num)))  # Convert number to string after removing sign
# print("Number of digits:", count)



# For small to medium numbers (most cases in Python):
# String method (len(str(num))) is faster.
# Reason: Python’s string conversion is highly optimized in C internally, whereas a while loop runs Python bytecode for each iteration, which is slower.

# For huge numbers (millions of digits):
# Division method may be faster memory-wise, because string conversion would need a large memory buffer for the digits.

