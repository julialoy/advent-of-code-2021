with open('day_1_puzzle_1.txt') as f:
    puzzle_input = f.read()

puzzle_input_parsed = puzzle_input.split('\n')

times_increased = 0
for i in range(0, len(puzzle_input_parsed)-1):
    if int(puzzle_input_parsed[i]) < int(puzzle_input_parsed[i+1]):
        times_increased += 1

print(times_increased)
