def check_each_cube_per_line(event):
    counts = {"red": 0, "green": 0, "blue": 0}
    for element in event.split(", "):
        amount, color = element.split()
        counts[color] = int(amount)
    return all(counts[color] <= limit
               for color, limit
               in {"red": 12, "green": 13, "blue": 14}.items())


def nheck_line_and_split(line):
    groups = line.strip().split(": ")[1].split("; ")
    return all(check_each_cube_per_line(group) for group in groups)


def calculate_total(file_path):
    total = 0
    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if nheck_line_and_split(line):
                total += i + 1
    return total


def calculate_minimum_cubes_and_power(file_path):
    with open(file_path, 'r') as file:
        games = file.read().strip().split('\n')

    total_power = 0

    for game_index, game in enumerate(games, start=1):
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}

        events = game.split('; ')
        for event in events:
            current_cubes = {'red': 0, 'green': 0, 'blue': 0}
            for cube_info in event.split(', '):
                try:
                    count, color = cube_info.split()
                    current_cubes[color] += int(count)
                except ValueError:
                    print(f"Error processing game {game_index}: '{cube_info}' is not in the expected format.")
                    return
            for color in min_cubes:
                min_cubes[color] = max(min_cubes[color], current_cubes[color])

        game_power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        total_power += game_power

    return total_power

# Replace 'files/day2in.txt' with your actual file path
total_power = calculate_minimum_cubes_and_power("files/day2in.txt")
print("Total Power:", total_power)
print(calculate_total("files/day2.txt"))
