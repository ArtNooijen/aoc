def find_minimum_cubes_per_event(event):
    counts = {"red": 0, "green": 0, "blue": 0}
    for element in event.split(", "):
        amount, color = element.split()
        counts[color] = max(counts[color], int(amount))
    return counts


def find_minimum_cubes_per_game(line):
    groups = line.strip().split(": ")[1].split("; ")
    min_cubes = {"red": 0, "green": 0, "blue": 0}
    for group in groups:
        counts = find_minimum_cubes_per_event(group)
        for color in min_cubes:
            min_cubes[color] = max(min_cubes[color], counts[color])
    return min_cubes


def calculate_total_power(file_path):
    total_power = 0
    with open(file_path, "r") as file:
        for line in file:
            min_cubes = find_minimum_cubes_per_game(line)
            power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
            total_power += power
    return total_power


print(calculate_total_power("files/day2.txt"))
