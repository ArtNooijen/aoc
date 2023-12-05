# Open and read the file content, then strip any leading/trailing whitespace
input_data = open("day1p1.txt", "r").read().strip()

# Initialize variables for storing the sum of the first and last numbers
sum_first_number = 0
sum_last_number = 0

# Define an array to map words to their corresponding numeric values
word_to_number = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

# Iterate through each line in the input data
for line in input_data.split("\n"):
    first_number_array = []
    last_number_array = []

    # Iterate over each character and its index in the line
    for i, char in enumerate(line):
        # Check if the character is a digit
        if char.isdigit():
            first_number_array.append(char)
            last_number_array.append(char)
        
        # Check for word numbers in the line
        for word, number in word_to_number.items():
            if line[i:].startswith(word):
                last_number_array.append(number)

    # Calculate the sum of the first and last digits/numbers
    sum_first_number += int(first_number_array[0] + first_number_array[-1])
    sum_last_number += int(last_number_array[0] + last_number_array[-1])

# Print the results
print(sum_first_number, sum_last_number)

