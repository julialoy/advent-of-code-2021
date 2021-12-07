with open('day_6_puzzle_input.txt') as f:
    fish = [int(num) for num in f.read().split(',')]

# Original, brute-force solution:
#
# days = 1
# while days <= 80:
#     previous_num_fish = len(fish)
#     for i in range(0, previous_num_fish):
#         if fish[i] == 0:
#             fish.append(8)
#         timer_value = fish[i] - 1
#         if timer_value < 0:
#             timer_value = 6
#         fish[i] = timer_value
#     days += 1
#
# print(len(fish))

# Solution used as part of puzzle 2:


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

print(sum_fish(fish_tracker(initial_fish_nums, 1, 80)))
