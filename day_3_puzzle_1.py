with open('day_3_puzzle_input.txt') as f:
    puzzle_input = f.read().splitlines()

bit_occur = {n: {1: 0, 0: 0} for n in range(0, len(puzzle_input[0]))}

for puzzle_str in puzzle_input:
    for i in range(0, len(puzzle_str)):
        if puzzle_str[i] == '1':
            bit_occur[i][0] += 1
        else:
            bit_occur[i][1] += 1

gamma_rate = ''
gamma_rate = gamma_rate.join(['1' if v[0] > v[1] else '0' for k,v in bit_occur.items()])
dec_gamma_rate = int(gamma_rate, 2)

epsilon_rate = ''
epsilon_rate = epsilon_rate.join(['1' if v[0] < v[1] else '0' for k,v in bit_occur.items()])
dec_epsilon_rate = int(epsilon_rate, 2)

print(f"Answer: {dec_gamma_rate * dec_epsilon_rate}")
