input = open("day1p1.txt", "r").read().strip()

first_number = 0
last_number = 0

for line in input.split("\n"):
    first_number_array = []
    last_number_array = []
    word_array = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i ,c in enumerate(line):
        if c.isdigit():
            first_number_array.append(c)
            last_number_array.append(c)
        for j ,word in enumerate(word_array):
            if line[i:].startswith(word):
                last_number_array.append(str(j+1))

    first_number += int(first_number_array[0] + first_number_array[-1])
    last_number += int(last_number_array[0] + last_number_array[-1])

print(first_number, last_number)
