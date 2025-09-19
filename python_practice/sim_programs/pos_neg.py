# 2) CHECK IF A NUMBER IS POSITIVE OR NEGATIVE NUMBER

n = int(input("Enter a number:"))
if (n >= 0):
    print("positive number.")
else:
    print("Negative number.")

  # TERNARY OPERATOR

n = int(input("Enter a number:"))
result = "positive number" if (n>=0) else "negative number"
print(result)