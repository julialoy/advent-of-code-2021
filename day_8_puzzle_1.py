with open('day_8_input.txt') as f:
    puzzle_input = f.read().splitlines()

signal_patterns = [patterns.split(' | ')[0].split(' ') for patterns in puzzle_input]

output_values = [values.split(' | ')[1].split(' ') for values in puzzle_input]

# Numbers that use unique segments:
# 1 (2 segments used)
# 4 (4 segments used)
# 7 (3 segments used)
# 8 (7 segments used)

nums_with_unique_segments = 0
total_values = 0
nums_without_unique_segments = 0

for value_set in output_values:
    for value in value_set:
        total_values += 1
        if len(value) == 2 or len(value) == 3 or len(value) == 4 or len(value) == 7:
            nums_with_unique_segments += 1
        elif len(value) == 5 or len(value) == 6:
            nums_without_unique_segments += 1

print(nums_with_unique_segments)

