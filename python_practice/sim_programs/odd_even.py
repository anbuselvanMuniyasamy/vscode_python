# 1) CHECK IF A NUMBER IS ODD OR EVEN.
    #  USING RECURSIVE FUNCTION.
n = int(input("Enter a number:"))
def check(n):
    if(n < 2):
        return (n % 2 == 0)
    return(check(n-2))
if check(n):
    print("Given Integer is Even.")
else:
    print("Given Integer is odd.")

#   # USING LAMBDA FUNCTION.

# number = int(input("Enter the Number:"))
# check_num = lambda number:"even" if number % 2 == 0 else "odd"
# result = check_num(number)
# print(result)