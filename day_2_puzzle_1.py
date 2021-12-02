# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

# Calculate the horizontal position and depth you would have after following the planned course.
# What do you get if you multiply your final horizontal position by your final depth?

with open('day_2_puzzle_input.txt') as f:
    puzzle_input = [ln.split(' ') for ln in f.read().splitlines()]

horiz = 0
vert = 0

for direction in puzzle_input:
    if direction[0] == 'forward':
        horiz += int(direction[1])
    elif direction[0] == 'down':
        vert += int(direction[1])
    else:
        vert -= int(direction[1])

print(horiz * vert)
