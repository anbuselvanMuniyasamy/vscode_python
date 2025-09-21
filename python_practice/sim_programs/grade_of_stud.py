# sub1 = float(input("Enter the mark of subject 1 : "))
# sub2 = float(input("Enter the mark of subject 2 : "))
# sub3 = float(input("Enter the mark of subject 3 : "))
# sub4 = float(input("Enter the mark of subject 4 : "))
# sub5 = float(input("Enter the mark of subject 5 : "))

# avg = (sub1+sub2+sub3+sub4+sub5)/5
# if avg >= 90:
#     print("Grade: A")
# elif avg >= 80 and avg < 90:
#     print("Grade: B")
# elif avg >= 70 and avg < 80:
#     print("Grade: C")
# elif avg >= 60 and avg < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")


    # other method using loop

#     # Ask the user how many subjects there are
num_subjects = int(input("Enter the number of subjects: "))

marks = []

for i in range(1, num_subjects + 1):
    mark = float(input(f"Enter the mark of subject {i}: "))
    marks.append(mark)

avg = sum(marks) / num_subjects
print(f"averge mark : {avg}")

if avg >= 90:
    print("Grade: A")
elif avg >= 80:
    print("Grade: B")
elif avg >= 70:
    print("Grade: C")
elif avg >= 60:
    print("Grade: D")
else:
    print("Grade: F")
