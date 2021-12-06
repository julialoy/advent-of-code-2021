with open('day_5_puzzle_input.txt') as f:
    puzzle_input = [ln.split(' -> ') for ln in f.read().splitlines()]

danger_points = {}
for ln in puzzle_input:
    start_coord = ln[0].split(',')
    end_coord = ln[1].split(',')
    # print(start_coord, end_coord)

    slope = 0
    if start_coord[0] != end_coord[0] and start_coord[1] != end_coord[1]:
        # print("Coords don't form a line")
        slope = abs((int(end_coord[1]) - int(start_coord[1])) / (int(end_coord[0]) - int(start_coord[0])))
        if slope != 1:
            continue
        # else:
        #     print(start_coord, end_coord, slope)

    if int(end_coord[0]) - int(start_coord[0]) > 0:
        starting_x = int(start_coord[0])
        ending_x = int(end_coord[0])
    else:
        starting_x = int(end_coord[0])
        ending_x = int(start_coord[0])

    if int(end_coord[1]) - int(start_coord[1]) > 0:
        starting_y = int(start_coord[1])
        ending_y = int(end_coord[1])
    else:
        starting_y = int(end_coord[1])
        ending_y = int(start_coord[1])

    if slope == 1:
        if int(start_coord[0]) > int(end_coord[0]):
            x_increase = -1
        else:
            x_increase = 1

        if int(start_coord[1]) > int(end_coord[1]):
            y_increase = -1
        else:
            y_increase = 1

        point = (int(start_coord[0]), int(start_coord[1]))
        if str(point) in danger_points.keys():
            danger_points[str(point)] += 1
        else:
            danger_points[str(point)] = 1

        while point != (int(end_coord[0]), int(end_coord[1])):
            point = (point[0]+x_increase, point[1]+y_increase)
            if str(point) in danger_points.keys():
                danger_points[str(point)] += 1
            else:
                danger_points[str(point)] = 1
            # Need to increase/decrease x and y by 1
            # beginning with first point until end up at
            # second point

    else:
        for i in range(starting_x, ending_x+1):
            for j in range(starting_y, ending_y+1):
                # print(f"adding point {(i, j)}")
                if str((i, j)) in danger_points.keys():
                    danger_points[str((i,j))] += 1
                else:
                    danger_points[str((i,j))] = 1

num_danger_points = 0
for k,v in danger_points.items():
    if v > 1:
        num_danger_points += 1

# print(danger_points)
print(num_danger_points)
