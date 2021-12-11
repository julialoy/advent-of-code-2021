with open('day_11_puzzle_input.txt') as f:
    octopuses = [list(num) for num in f.read().splitlines()]


def increase_octopus(octopuses):
    for i in range(0, len(octopuses)):
        for j in range(0, len(octopuses[0])):
            num_octo = int(octopuses[i][j])
            num_octo += 1
            octopuses[i][j] = num_octo
    return octopuses


def reset_flashed_octopuses(octo_lst):
    for i in range(0, len(octo_lst)):
        for j in range(0, len(octo_lst[i])):
            if octo_lst[i][j] > 9:
                octo_lst[i][j] = 0
    return octo_lst


def flash_octopuses(octopuses, flash_coords):
    num_coords = len(flash_coords)
    for y in range(0, len(octopuses)):
        for x in range(0, len(octopuses[0])):
            if octopuses[y][x] > 9:
                if (y, x) not in flash_coords:
                    flash_coords.append((y, x))
                    if y != 0:
                        octopuses[y-1][x] += 1
                    if y != len(octopuses)-1:
                        octopuses[y+1][x] += 1
                    if x != 0:
                        octopuses[y][x-1] += 1
                    if x != len(octopuses[0])-1:
                        octopuses[y][x+1] += 1
                    if y != 0 and x != 0:
                        octopuses[y-1][x-1] += 1
                    if y != len(octopuses)-1 and x != 0:
                        octopuses[y+1][x-1] += 1
                    if y != 0 and x != len(octopuses[0])-1:
                        octopuses[y-1][x+1] += 1
                    if y != len(octopuses)-1 and x != len(octopuses[0])-1:
                        octopuses[y+1][x+1] += 1
    # print(f"Number octopuses flashed: {len(flash_coords)}")

    if num_coords == len(flash_coords):
        return octopuses, flash_coords
    else:
        return flash_octopuses(octopuses, flash_coords)


octopuses_flashing = 0
step = 0
# print(octopuses)
while octopuses_flashing != 100:
    increased_octopuses = increase_octopus(octopuses)
    octopuses, flashed_octopuses = flash_octopuses(increased_octopuses, [])
    octopuses = reset_flashed_octopuses(octopuses)
    step += 1
    octopuses_flashing = len(flashed_octopuses)
    # print(f"STEP: {step}")

print(octopuses_flashing)
print(step)
# print(octopuses)
