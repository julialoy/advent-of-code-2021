with open('day_6_puzzle_input.txt') as f:
    fish = [int(num) for num in f.read().split(',')]


def fish_tracker(fish_nums, start_day, total_days):
    if total_days < start_day:
        return fish_nums

    prev_temp_value = fish_nums[-1][1]
    for i in range(len(fish_nums)):
        curr_temp_value = fish_nums[i][1]
        new_fish_tuple = (fish_nums[i][0], prev_temp_value)
        fish_nums[i] = new_fish_tuple

        if fish_nums[i][0] == 0:
            six_fish_value = fish_nums[2][1] + curr_temp_value
            fish_nums[2] = (fish_nums[2][0], six_fish_value)

        prev_temp_value = curr_temp_value

    start_day += 1
    return fish_tracker(fish_nums, start_day, total_days)


def sum_fish(final_fish_lst):
    return sum(n for _, n in final_fish_lst)


initial_fish_nums = [(i, 0) for i in range(8, -1, -1)]
for t in initial_fish_nums:
    if t[0] in fish:
        new_num = len([x for x in fish if x == t[0]])
        initial_fish_nums[initial_fish_nums.index(t)] = (t[0], new_num)

print(f"Original fish list: {initial_fish_nums}")
print(sum_fish(fish_tracker(initial_fish_nums, 1, 256)))
