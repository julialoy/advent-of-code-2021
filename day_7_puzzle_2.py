with open('day_7_puzzle_input.txt') as f:
    crab_positions = [int(num) for num in f.read().split(',')]


def calculate_best_pos(positions, target_position):
    total_fuel = 0
    for horiz_pos in positions:
        if horiz_pos > target_position:
            initial_fuel_used = (horiz_pos - target_position)
            final_fuel_used = sum(range(1, initial_fuel_used+1))
            total_fuel += final_fuel_used
        else:
            initial_fuel_used = (target_position - horiz_pos)
            final_fuel_used = sum(range(1, initial_fuel_used+1))
            total_fuel += final_fuel_used
    return total_fuel


crab_positions.sort()
max_crab = max(crab_positions)
min_crab = min(crab_positions)
crab_pos_set = set(x for x in range(min_crab, max_crab+1))

lowest_fuel_expenditure = None
optimal_horiz_pos = None
for pos in crab_pos_set:
    fuel_expended = calculate_best_pos(crab_positions, pos)
    if lowest_fuel_expenditure is None or fuel_expended < lowest_fuel_expenditure:
        lowest_fuel_expenditure = fuel_expended
        optimal_horiz_pos = pos

print(f"Lowest amount of fuel used: {lowest_fuel_expenditure}")
print(f"Best horizontal position: {optimal_horiz_pos}")

