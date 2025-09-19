# # Fibonacci Series in Python using While Loop
 
# n = int(input("How many Fibonacci numbers to print? "))

# a, b = 0, 1
# for _ in range(n):
#     print(a, end=' ')
#     a, b = b, a + b

  # using recursion 
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

n = int(input("How many Fibonacci numbers to print? "))
result = fibonacci(n)
print(result)  # if you want to remove the bracket use this ==> print(*result)
