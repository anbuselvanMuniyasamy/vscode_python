# # Fibonacci Series in Python using While Loop
 
n = int(input("Enter how many terms: "))

a, b = 0, 1   # first two terms
count = 0

print("Fibonacci series:")

while count < n:
    print(a, end=" ")   # print current term
    c = a + b           # next term = sum of previous two
    a = b               # move a to next
    b = c               # move b to next
    count += 1



  # using recursion 
# def fibonacci(n):
#     if n == 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         seq = fibonacci(n - 1)
#         seq.append(seq[-1] + seq[-2])
#         return seq

# n = int(input("How many Fibonacci numbers to print? "))
# result = fibonacci(n)
# print(result)  # if you want to remove the bracket use this ==> print(*result)
