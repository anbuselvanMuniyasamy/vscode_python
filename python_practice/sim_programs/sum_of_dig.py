num = int(input("Enter the number : "))
sum_dig = 0
while(num>0):
    dig = num % 10
    sum_dig += dig
    num = num // 10
print("sum of the digits : ",sum_dig)

   # USING RECURSION

num = int(input("Enter the number : "))
def sum_dig(num):
    if num==0:
        return 0
    else:
        return num%10 + sum_dig(num//10)
print("Sum of digits",sum_dig(num))

