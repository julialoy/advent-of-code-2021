with open('day_5_puzzle_input.txt') as f:
    puzzle_input = [ln.split(' -> ') for ln in f.read().splitlines()]

danger_points = {}
for ln in puzzle_input:
    start_coord = ln[0].split(',')
    end_coord = ln[1].split(',')
    # print(start_coord, end_coord)

    if start_coord[0] != end_coord[0] and start_coord[1] != end_coord[1]:
        # print("Coords don't form a line")
        continue

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

print(num_danger_points)
