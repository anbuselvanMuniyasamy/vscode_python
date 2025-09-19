# 3) PRINT ALL ODD NUMBERS IN GIVEN RANGE

lower_range = int(input("Enter the First range : "))
upper_range = int(input("Enter the last range : "))
for i in range(lower_range,upper_range+1):
    if(i%3==0):
        print(i)