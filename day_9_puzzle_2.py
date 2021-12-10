with open('day_9_puzzle_input.txt') as f:
    puzzle_input = [list(ln) for ln in f.read().splitlines()]


low_points = []
for i in range(0, len(puzzle_input)):
    for j in range(0, len(puzzle_input[i])):
        if i == 0 and j == 0:
            if puzzle_input[i][j] < puzzle_input[i][j+1] and puzzle_input[i][j] < puzzle_input[i+1][j]:
                low_points.append((i, j))
        elif i == 0 and j == len(puzzle_input[i])-1:
            if puzzle_input[i][j] < puzzle_input[i][j-1] and puzzle_input[i][j] < puzzle_input[i+1][j]:
                low_points.append((i, j))
        elif i == 0:
            if puzzle_input[i][j] < puzzle_input[i][j-1] and puzzle_input[i][j] < puzzle_input[i+1][j] and puzzle_input[i][j] < puzzle_input[i][j+1]:
                low_points.append((i, j))
        elif i == len(puzzle_input)-1 and j == 0:
            if puzzle_input[i][j] < puzzle_input[i][j+1] and puzzle_input[i][j] < puzzle_input[i-1][j]:
                low_points.append((i, j))
        elif i == len(puzzle_input)-1 and j == len(puzzle_input[i])-1:
            if puzzle_input[i][j] < puzzle_input[i][j-1] and puzzle_input[i][j] < puzzle_input[i-1][j]:
                low_points.append((i, j))
        elif i == len(puzzle_input)-1:
            if puzzle_input[i][j] < puzzle_input[i][j-1] and puzzle_input[i][j] < puzzle_input[i][j+1] and puzzle_input[i][j] < puzzle_input[i-1][j]:
                low_points.append((i, j))
        elif j == 0:
            if puzzle_input[i][j] < puzzle_input[i+1][j] and puzzle_input[i][j] < puzzle_input[i-1][j] and puzzle_input[i][j] < puzzle_input[i][j+1]:
                low_points.append((i, j))
        elif j == len(puzzle_input[i])-1:
            if puzzle_input[i][j] < puzzle_input[i+1][j] and puzzle_input[i][j] < puzzle_input[i-1][j] and puzzle_input[i][j] < puzzle_input[i][j-1]:
                low_points.append((i, j))
        else:
            if puzzle_input[i][j] < puzzle_input[i][j - 1] and puzzle_input[i][j] < puzzle_input[i][j + 1] and \
                    puzzle_input[i][j] < puzzle_input[i - 1][j] and puzzle_input[i][j] < puzzle_input[i+1][j]:
                low_points.append((i, j))


def find_top_limit(point, puzzle):
    x_coord = int(point[1])
    y_coord = int(point[0])

    if y_coord == 0:
        limit = (int(point[0]), int(point[1]))
        return limit

    for i in range(y_coord, 0, -1):
        if int(puzzle[i][x_coord]) == 9:
            limit = (i, x_coord)
            return limit

    limit = (0, x_coord)
    return limit


def find_bottom_limit(point, puzzle):
    x_coord = int(point[1])
    y_coord = int(point[0])

    if y_coord == len(puzzle)-1:
        limit = (int(point[0]), int(point[1]))
        return limit

    for i in range(y_coord, len(puzzle)):
        if int(puzzle[i][x_coord]) == 9:
            limit = (i, x_coord)
            return limit

    limit = (len(puzzle)-1, x_coord)
    return limit


def find_home_left_limit(point, puzzle):
    x_coord = int(point[1])
    y_coord = int(point[0])

    if x_coord == 0:
        limit = (int(point[0]), int(point[1]))
        return limit

    for i in range(x_coord, 0, -1):
        if int(puzzle[y_coord][i]) == 9:
            limit = (y_coord, i)
            return limit

    limit = (y_coord, 0)
    return limit


def find_home_right_limit(point, puzzle):
    x_coord = int(point[1])
    y_coord = int(point[0])

    if x_coord == len(puzzle)-9:
        limit = (y_coord, x_coord)
        return limit

    for i in range(x_coord, len(puzzle[0])):
        if int(puzzle[y_coord][i]) == 9:
            limit = (y_coord, i)
            return limit

    limit = (y_coord, len(puzzle[0])-1)
    return limit


def find_top_left_limit(top_limit, home_left_limit, puzzle):
    x_coord = top_limit[1]
    y_coord = top_limit[0]

    if x_coord == 0:
        limit = top_limit
        return limit
    elif int(puzzle[y_coord][x_coord]) == 9 and home_left_limit == x_coord:
        limit = top_limit
        return limit

    for i in range(x_coord, 0, -1):
        if int(puzzle[y_coord][i]) == 9:
            limit = (y_coord, i)
            return limit

    limit = (y_coord, 0)
    return limit


def find_top_right_limit(top_limit, home_right_limit, puzzle):
    x_coord = top_limit[1]
    y_coord = top_limit[0]

    if x_coord == len(puzzle[0])-1:
        limit = top_limit
        return limit
    elif int(puzzle[y_coord][x_coord]) == 9 and home_right_limit == x_coord:
        limit = top_limit
        return limit

    for i in range(x_coord, len(puzzle[0])):
        if int(puzzle[y_coord][i]) == 9:
            limit = (y_coord, i)
            return limit

    limit = (y_coord, len(puzzle[0])-1)
    return limit


def find_bottom_left_limit(bottom_limit, home_bottom_limit, puzzle):
    x_coord = bottom_limit[1]
    y_coord = bottom_limit[0]

    if x_coord == 0:
        limit = bottom_limit
        return limit
    elif int(puzzle[y_coord][x_coord]) == 9 and home_bottom_limit == x_coord:
        limit = bottom_limit
        return limit

    for i in range(x_coord, 0, -1):
        print(f"FIND BOTTOM LEFT LIMIT, XCOORD: {i}, POINT: {puzzle[y_coord][i]}")
        if int(puzzle[y_coord][i]) == 9:
            limit = (y_coord, i)
            return limit

    limit = (y_coord, 0)
    print(f"GOT TO BEGINNING OF LINE, NO 9 FOUND. LIMIT = {limit}")
    return limit


def find_bottom_right_limit(bottom_limit, home_right_limit, puzzle):
    x_coord = bottom_limit[1]
    y_coord = bottom_limit[0]

    if x_coord == len(puzzle[0])-1:
        limit = bottom_limit
        return limit
    elif int(puzzle[y_coord][x_coord]) == 9 and home_right_limit == x_coord:
        limit = bottom_limit
        return limit

    for i in range(x_coord, len(puzzle[0])-1):
        if int(puzzle[y_coord][i]) == 9:
            limit = (y_coord, i)
            return limit

    limit = (y_coord, len(puzzle[0])-1)
    return limit


def fill_in_basin(point, top_limit, bottom_limit, puzzle):
    fill = []

    for y in range(top_limit[0], bottom_limit[0]+1):
        for x1 in range(int(point[1]), -1, -1):
            if int(puzzle[y][x1]) != 9 and (y, x1) not in fill:
                fill.append((y, x1))
            else:
                break
        for x2 in range(int(point[1]), len(puzzle[0])):
            if int(puzzle[y][x2]) != 9 and (y, x2) not in fill:
                fill.append((y, x2))
            else:
                break

    for point in fill:
        y = point[0]
        x = point[1]
        if y-1 >= 0:
            if int(puzzle[y-1][x]) != 9 and (y-1, x) not in fill:
                fill.append((y-1, x))
        if y+1 < len(puzzle):
            if int(puzzle[y+1][x]) != 9 and (y+1, x) not in fill:
                fill.append((y+1, x))
        if x-1 >= 0:
            if int(puzzle[y][x-1]) != 9 and (y, x-1) not in fill:
                fill.append((y, x-1))
        if x+1 < len(puzzle[0]):
            if int(puzzle[y][x+1]) != 9 and (y, x+1) not in fill:
                fill.append((y, x+1))

    return fill

basins = []
for low_point in low_points:
    # find upper limit
    # find down limit
    # find right limit
    # find left limit
    upper_limit = find_top_limit(low_point, puzzle_input)
    lower_limit = find_bottom_limit(low_point, puzzle_input)
    # left_limit = find_home_left_limit(low_point, puzzle_input)
    # right_limit = find_home_right_limit(low_point, puzzle_input)
    # upper_left_limit = find_top_left_limit(upper_limit, left_limit, puzzle_input)
    # upper_right_limit = find_top_right_limit(upper_limit, right_limit, puzzle_input)
    # lower_right_limit = find_bottom_right_limit(lower_limit, right_limit, puzzle_input)
    # lower_left_limit = find_bottom_left_limit(lower_limit, left_limit, puzzle_input)
    fill_points = (fill_in_basin(low_point, upper_limit, lower_limit, puzzle_input))
    # print(f"Low point = {low_point}, "
    #       f"upper limit = {upper_limit}, "
    #       f"upper left = {upper_left_limit}, "
    #       f"upper right = {upper_right_limit}, "
    #       f"lower limit = {lower_limit}, "
    #       f"lower left = {lower_left_limit}, "
    #       f"lower right = {lower_right_limit}, "
    #       f"right limit = {right_limit}, "
    #       f"left limit = {left_limit} ")
    basins.append(len(fill_points))

largest = 0
second_largest = 0
third_largest = 0
for basin in basins:
    if basin > largest:
        third_largest = second_largest
        second_largest = largest
        largest = basin
    elif largest >= basin > second_largest:
        third_largest = second_largest
        second_largest = basin
    elif second_largest >= basin > third_largest:
        third_largest = basin

print(largest * second_largest * third_largest)

