with open('day_10_puzzle_input.txt') as f:
    puzzle_input = [list(ln) for ln in f.read().splitlines()]

total_illegal_chars = []
illegal_lines = []
incomplete_lines = []
incomplete_chars = []
coord_char_dict = {']': '[', '}': '{', ')': '(', '>': '<'}
for line in puzzle_input:
    open_chars = []
    for i in range(0, len(line)):
        if line[i] not in coord_char_dict.keys():
            open_chars.append(line[i])
        elif i == len(line)-1 and len(open_chars) == 0:
            if line[i] in coord_char_dict.keys():
                illegal_lines.append(line)
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

    if line not in illegal_lines and len(open_chars) > 0:
        incomplete_lines.append(line)
        incomplete_chars.append(open_chars)


completion_dict = {'[': ']', '<': '>', '(': ')', '{': '}'}
chars_for_completion = []
for lst in incomplete_chars:
    completion_chars = []
    for x in range(len(lst)-1, -1, -1):
        completion_chars.append(completion_dict[lst[x]])
    chars_for_completion.append(completion_chars)

char_points = {')': 1, ']': 2, '}': 3, '>': 4}
total_scores = []
for char_lst in chars_for_completion:
    total_score = 0
    for c in char_lst:
        temp_score = total_score * 5
        # print(f"{total_score} * 5 = {temp_score}")
        temp_score += char_points[c]
        # print(f"+ {char_points[c]} = {temp_score}")
        total_score = temp_score
    total_scores.append(total_score)

sorted_scores = sorted(total_scores)
# print(chars_for_completion)
# print(len(incomplete_lines))
# print(total_scores)
# print(sorted_scores)
print(sorted_scores[(len(sorted_scores) // 2)])
