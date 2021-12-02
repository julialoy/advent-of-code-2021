# down X increases your aim by X units.
# up X decreases your aim by X units.
# forward X does two things:
# It increases your horizontal position by X units.
# It increases your depth by your aim multiplied by X.

# Again note that since you're on a submarine, down and up do the opposite of what you might expect:
# "down" means aiming in the positive direction.

# Using this new interpretation of the commands, calculate the horizontal position and depth you would have after
# following the planned course. What do you get if you multiply your final horizontal position by your final depth?

with open('day_2_puzzle_input.txt') as f:
    puzzle_input = [ln.split(' ') for ln in f.read().splitlines()]

horiz = 0
depth = 0
aim = 0

for direction in puzzle_input:
    if direction[0] == 'down':
        aim += int(direction[1])
    elif direction[0] == 'up':
        aim -= int(direction[1])
    else:
        horiz += int(direction[1])
        depth += (aim * int(direction[1]))

print(horiz * depth)
