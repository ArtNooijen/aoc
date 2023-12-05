input_data = open("day1p1.txt", "r").read().strip()

sum_first_number = 0
sum_last_number = 0

word_to_number = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

for line in input_data.split("\n"):
    first_number_array = []
    last_number_array = []

    for i, char in enumerate(line):
        if char.isdigit():
            first_number_array.append(char)
            last_number_array.append(char)
        
        for word, number in word_to_number.items():
            if line[i:].startswith(word):
                last_number_array.append(number)

    sum_first_number += int(first_number_array[0] + first_number_array[-1])
    sum_last_number += int(last_number_array[0] + last_number_array[-1])

print(sum_first_number, sum_last_number)

