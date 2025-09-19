# class Bird:
#     def fly(self):
#         print("Birds can fly")

# class Penguin(Bird):
#     def fly(self):  # Overriding
#         print("Penguins cannot fly")

# b1 = Bird()
# b2 = Penguin()

# b1.fly()  # Birds can fly
# b2.fly()  # Penguins cannot fly

# def my_function():
#     x = 10  # local variable
#     print("Inside function:", x)

# my_function()

# x = 50  # global variable

# def my_function():
#     print("Inside function:", x)

# my_function()       # 50
# print("Outside function:", x)  

# x = 10  # global variable

# def modify_global():
#     global x
#     x = 20  # modify global variable

# print("Before:", x)   # 10
# modify_global()
# print("After:", x)    