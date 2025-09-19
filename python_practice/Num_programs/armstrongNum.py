n = int(input("Enter a number: "))
digits = list(map(int, str(n)))
cubes = list(map(lambda x: x**3, digits))

if sum(cubes) == n:
    print("It's an Armstrong number.")
else:
    print("It's not an Armstrong number.")

