with open('day_1_puzzle_1.txt') as f:
    puzzle_input = f.read()

# test_puzzle_input = """199
# 200
# 208
# 210
# 200
# 207
# 240
# 269
# 260
# 263"""
# parsed_test = test_puzzle_input.split('\n')
parsed_input = puzzle_input.split('\n')
times_increased = 0

for i in range(0, len(parsed_input)-3):
    window_a = sum([int(parsed_input[i]), int(parsed_input[i+1]), int(parsed_input[i+2])])
    window_b = sum([int(parsed_input[i+1]), int(parsed_input[i+2]), int(parsed_input[i+3])])
    if window_a < window_b:
        times_increased += 1

print(times_increased)
