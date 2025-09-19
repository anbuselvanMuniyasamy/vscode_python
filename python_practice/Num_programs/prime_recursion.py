
# num = int(input("Enter number: "))

# def is_prime(n, divisor=2):
#     if n <= 1:
#         return False
#     if divisor == n:
#         return True
#     if n % divisor == 0:
#         return False
#     return is_prime(n, divisor + 1)

# if is_prime(num):
#     print("Number is prime")
# else:
#     print("Number is not prime")

  # with range

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

def is_prime(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return is_prime(n, divisor + 1)

print(f"Prime numbers between {start} and {end} are:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num)










