with open('day_9_puzzle_input.txt') as f:
    puzzle_input = [list(ln) for ln in f.read().splitlines()]


low_points = []
for i in range(0, len(puzzle_input)):
    for j in range(0, len(puzzle_input[i])):
        if i == 0 and j == 0:
            if puzzle_input[i][j] < puzzle_input[i][j+1] and puzzle_input[i][j] < puzzle_input[i+1][j]:
                low_points.append(puzzle_input[i][j])
        elif i == 0 and j == len(puzzle_input[i])-1:
            if puzzle_input[i][j] < puzzle_input[i][j-1] and puzzle_input[i][j] < puzzle_input[i+1][j]:
                low_points.append(puzzle_input[i][j])
        elif i == 0:
            if puzzle_input[i][j] < puzzle_input[i][j-1] and puzzle_input[i][j] < puzzle_input[i+1][j] and puzzle_input[i][j] < puzzle_input[i][j+1]:
                low_points.append(puzzle_input[i][j])
        elif i == len(puzzle_input)-1 and j == 0:
            if puzzle_input[i][j] < puzzle_input[i][j+1] and puzzle_input[i][j] < puzzle_input[i-1][j]:
                low_points.append(puzzle_input[i][j])
        elif i == len(puzzle_input)-1 and j == len(puzzle_input[i])-1:
            if puzzle_input[i][j] < puzzle_input[i][j-1] and puzzle_input[i][j] < puzzle_input[i-1][j]:
                low_points.append(puzzle_input[i][j])
        elif i == len(puzzle_input)-1:
            if puzzle_input[i][j] < puzzle_input[i][j-1] and puzzle_input[i][j] < puzzle_input[i][j+1] and puzzle_input[i][j] < puzzle_input[i-1][j]:
                low_points.append(puzzle_input[i][j])
        elif j == 0:
            if puzzle_input[i][j] < puzzle_input[i+1][j] and puzzle_input[i][j] < puzzle_input[i-1][j] and puzzle_input[i][j] < puzzle_input[i][j+1]:
                low_points.append(puzzle_input[i][j])
        elif j == len(puzzle_input[i])-1:
            if puzzle_input[i][j] < puzzle_input[i+1][j] and puzzle_input[i][j] < puzzle_input[i-1][j] and puzzle_input[i][j] < puzzle_input[i][j-1]:
                low_points.append(puzzle_input[i][j])
        else:
            if puzzle_input[i][j] < puzzle_input[i][j - 1] and puzzle_input[i][j] < puzzle_input[i][j + 1] and \
                    puzzle_input[i][j] < puzzle_input[i - 1][j] and puzzle_input[i][j] < puzzle_input[i+1][j]:
                low_points.append(puzzle_input[i][j])

risk_level = 0
for point in low_points:
    risk_level += (int(point) + 1)

print(risk_level)
