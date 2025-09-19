  # Python Program to Remove Odd Indexed Characters in a string


text = input("Enter a string: ")

def remove_odd_indexed_chars(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:  # even index
            result += s[i]
    return result

result = remove_odd_indexed_chars(text)
print("String after removing odd-indexed characters:", result)


   # other   (FASTER THAN LOOP)
text = input("Enter a string: ")

def remove_odd_indexed_chars(s):
    return s[::2] 

# Example usage

result = remove_odd_indexed_chars(text)
print("String after removing odd-indexed characters:", result)


# Key part: s[::2]
# This is called string slicing in Python.

# The syntax s[start:stop:step] means:

# start: where to begin (default is 0)

# stop: where to end (default is end of the string)

# step: how many characters to skip each time

# So s[::2] means:

# Start at index 0

# Go till the end

# Take every 2nd character (skip one character each time)
