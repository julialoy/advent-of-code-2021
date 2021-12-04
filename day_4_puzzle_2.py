with open('day_4_puzzle_input.txt') as f:
    puzzle_input = f.read().split('\n\n')


def is_there_winner(bingo_boards_dict, boards_already_won):
    winning_board = None
    winning_coords = []
    is_winner = False
    for k,v in bingo_boards_dict.items():
        if k in boards_already_won:
            # print(f"Board {k} already won, do not check")
            continue
        # print(f"Checking board{k}, coords: {v}")
        if is_winner:
            break
        for i in range(0, 5):
            if is_winner:
                break
            times_found_r = 0
            times_found_c = 0
            for coord in v:
                if is_winner:
                    break
                if i == coord[0]:
                    times_found_r += 1
                if i == coord[1]:
                    times_found_c += 1
            # print(f"In board {k}, times {i} found in row = {times_found_r} times {i} found in col = {times_found_c}")
            if times_found_r == 5:
                winning_board = k
                winning_coords = [coord for coord in v if coord[0] == i]
                is_winner = True
                break
            elif times_found_c == 5:
                winning_board = k
                winning_coords = [coord for coord in v if coord[1] == i]
                is_winner = True
                break

    if winning_board is not None:
        return winning_board, winning_coords
    else:
        return None, None


def get_winning_nums(win_board, win_coords):
    nums = []
    for c in win_coords:
        nums.append(win_board[c[0]][c[1]])
    return nums


def sum_uncalled_nums(b_board, last_called_num, called_nums_list):
    uncalled_nums = []
    board_nums = []
    nums_called = called_nums_list[:called_nums_list.index(last_called_num)+1]
    for row in b_board:
        for i in range(0, 5):
            board_nums.append(row[i])

    for x in board_nums:
        if x not in nums_called:
            uncalled_nums.append(x)

    return sum(uncalled_nums)


called_nums = [int(n) for n in puzzle_input[0].split(',')]

bingo_board = {}
for index in range(1, len(puzzle_input)):
    board = []
    temp_board = puzzle_input[index].split('\n')
    for ln in temp_board:
        board.append([int(n) for n in ln.split(' ') if n != ''])
    bingo_board[index] = board

played_boards = {}
winning_boards = []
last_num_called = None
# print(len(bingo_board))
for num in called_nums:
    if len(winning_boards) == len(bingo_board):
        # print(f"Length winners: {len(winning_boards)}, num bingo boards: {len(bingo_board)}")
        break
    # print(f"Calling number: {num}, boards won: {winning_boards}")
    # winner_found = False
    for k,v in bingo_board.items():
        # print(f"Now checking board: {k}")
        # if winner_found:
        #     break
        if k in winning_boards:
            # print(f"Skip this board ({k})")
            continue
        for i in range(0, len(v)):
            # if winner_found:
            #     break
            if num in v[i]:
                num_coords = [i, v[i].index(num)]
                # print(f"Added {num} ({[i, v[i].index(num)]}) for board {k}")
                if k not in played_boards:
                    played_boards[k] = [num_coords]
                else:
                    played_boards[k].append(num_coords)

                bingo_winner, winning_coordinates = is_there_winner(played_boards, winning_boards)
                if bingo_winner is not None:
                    # print(f"bingo winner is: {bingo_winner}")
                    winning_nums = get_winning_nums(bingo_board[bingo_winner], winning_coordinates)
                    # winner_found = True
                    winning_boards.append(k)
                    last_num_called = num
                    # print(f"Last winning number: {last_num_called}, winning board is {k}, winning numbers: {winning_nums}")
                    # break

sum_unmarked = sum_uncalled_nums(bingo_board[winning_boards[-1]], last_num_called, called_nums)
print(f"Sum unmarked numbers from winning board: {sum_unmarked}")
print(f"Final score from winning board: {sum_unmarked * last_num_called}")
