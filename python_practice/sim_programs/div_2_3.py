start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

print("Numbers are not divisible by 2 and 3 are:")
for i in range(start, end + 1):
    if(i % 2 != 0 and i % 3 != 0):
        print(i)

        # div by 7 and mul of 5

# start = int(input("Enter the start number: "))
# end = int(input("Enter the end number: "))
# print("Numbers divisible by 7 and multiple by 5 are:")
# for i in range(start, end + 1):
#     if (i % 7 == 0 and i % 5 == 0) :
#         print(i)

#
 
# lower=int(input("Enter lower range limit:"))
# upper=int(input("Enter upper range limit:"))
# num=int(input("Enter the number to be divided by:"))
# for i in range(lower,upper+1):
#     if(i%num==0):
#         print(i)


