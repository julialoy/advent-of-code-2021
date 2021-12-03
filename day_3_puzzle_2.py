with open('day_3_puzzle_input.txt') as f:
    puzzle_input = f.read().splitlines()


def find_common_bit(bit_occur_dict, rating_type):
    if rating_type == 'oxygen':
        if bit_occur_dict['1'] > bit_occur_dict['0']:
            common_bit = '1'
        elif bit_occur_dict['1'] < bit_occur_dict['0']:
            common_bit = '0'
        else:
            common_bit = '1'
    else:
        if bit_occur_dict['1'] < bit_occur_dict['0']:
            common_bit = '1'
        elif bit_occur_dict['1'] > bit_occur_dict['0']:
            common_bit = '0'
        else:
            common_bit = '0'

    return common_bit


def find_rating(puzzle, index, rating_type):
    if len(puzzle) == 1:
        return puzzle

    bit_occur = {'1': 0, '0': 0}

    for puzzle_str in puzzle:
        if puzzle_str[index] == '1':
            bit_occur['1'] += 1
        else:
            bit_occur['0'] += 1

    common_bit = find_common_bit(bit_occur, rating_type)
    puzzle = [puzzle_str for puzzle_str in puzzle if puzzle_str[index] == common_bit]
    return find_rating(puzzle, index+1, rating_type)


oxygen_gen_rating = find_rating(puzzle_input, 0, 'oxygen')
co2_scrub_rating = find_rating(puzzle_input, 0, 'co2')
life_support_rating = int(oxygen_gen_rating[0], 2) * int(co2_scrub_rating[0], 2)

print(life_support_rating)
