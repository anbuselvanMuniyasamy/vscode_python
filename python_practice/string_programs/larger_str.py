def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

def larger_string(str1, str2):
    len1 = string_length(str1)
    len2 = string_length(str2)

    if len1 > len2:
        return str1
    elif len2 > len1:
        return str2
    else:
        return "Both strings are of equal length."

# Example usage:
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = larger_string(s1, s2)
print("Larger string:", result)
