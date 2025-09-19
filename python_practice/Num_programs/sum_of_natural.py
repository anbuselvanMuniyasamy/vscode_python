n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("The sum of first n natural numbers is", total)


#  # other easy method (faster)
# n = int(input("Enter a number: "))
# total = n * (n + 1) // 2
# print("The sum of first n natural numbers is", total)
