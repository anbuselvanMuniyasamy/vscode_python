def count_up_to(maximum):
    count = 1
    while count <= maximum:
        yield count
        count += 1
counter = count_up_to(5)
for number in count_up_to(5):
    print(number)
