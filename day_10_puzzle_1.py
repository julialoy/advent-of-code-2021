with open('day_10_puzzle_input.txt') as f:
    puzzle_input = [list(ln) for ln in f.read().splitlines()]

total_illegal_chars = []
illegal_lines = []
incomplete_lines = []
coord_char_dict = {']': '[', '}': '{', ')': '(', '>': '<'}
for line in puzzle_input:
    open_chars = []
    for i in range(0, len(line)):
        if line[i] not in coord_char_dict.keys():
            open_chars.append(line[i])
        else:
            if len(open_chars) < 1:
                total_illegal_chars.append(line[i])
                illegal_lines.append(line)
                break
            elif open_chars[-1] != coord_char_dict[line[i]]:
                total_illegal_chars.append(line[i])
                illegal_lines.append(line)
                break
            else:
                open_chars.pop()


char_value = {')': 3, ']': 57, '}': 1197, '>': 25137}
illegal_char_value = 0
for c in total_illegal_chars:
    illegal_char_value += char_value[c]

print(illegal_char_value)
