with open('day_8_input.txt') as f:
    puzzle_input = f.read().splitlines()


def find_right_segments(pattern_lst):
    """Finds the two characters that are the top-right and
    bottom-right segments but cannot distinguish which is which.
    """
    right_segments = None
    for p in pattern_lst:
        if len(p) == 2:
            right_segments = set(p)
            # print(f"Found right segments: {right_segments}")
    # right_seg_chars = ''
    # for char in right_segments:
    #     right_seg_chars = right_seg_chars + char
    # print(f"Returning right segments: {right_seg_chars}")
    # return right_seg_chars
    return right_segments


def find_top_segment(pattern_lst, right_segs):
    top_segment = ''
    for p in pattern_lst:
        if len(p) == 3:
            # top_segment = set(p).difference(set(right_segs))
            top_segment = set(p).difference(right_segs)
            # print(f"Found top segment: {top_segment}")
    # top_char = ''
    # for char in top_segment:
    #     top_char = char
    #
    # print(f"Returning top segment: {top_char}")
    # return top_char
    return top_segment


def find_lefttopmiddle_segments(pattern_lst, right_segs):
    """Finds the two characters that are the left-top and
    middle segments but cannot distinguish which is which.
    """
    left_top_middle_segments = ''
    for p in pattern_lst:
        if len(p) == 4:
            # left_top_middle_segments = set(p).difference(set(right_segs))
            left_top_middle_segments = set(p).difference(right_segs)
            # print(f"Found top-left and middle segments: {left_top_middle_segments}")
    # left_top_middle_chars = ''
    # for char in left_top_middle_segments:
    #     left_top_middle_chars = left_top_middle_chars + char
    # print(f"Returning left-top and middle chars: {left_top_middle_chars}")
    # return left_top_middle_chars
    return left_top_middle_segments


def find_topleft_middle_bottom_segments(pattern_lst, right_segs, top_seg, left_top_middle_segs):
    top_left_segment = ''
    middle_segment = ''
    bottom_segment = ''
    for p in pattern_lst:
        if len(p) == 5:
            # print(f"Found length 5: {p}")
            # if right_segs in p and top_seg in p:
            #     middle_bottom_segs = (set(p) | set(right_segs) | set(top_seg)) - (
            #                 set(p) & set(right_segs) & set(top_seg))
            if len(set(p) & ((set(p)&right_segs) | (set(p)&top_seg))) == 3:
                # print(f" For {p}: {(set(p)) & ((set(p)&right_segs) | (set(p)&top_seg))}")
                middle_bottom_segs = set(p) - ((set(p)|right_segs|top_seg) & ((set(p)&right_segs) | (set(p)&top_seg)))
                # print(f"Found middle and bottom segments: {middle_bottom_segs}")
                top_left_segment = (set(left_top_middle_segs)).difference(middle_bottom_segs)
                # print(f"Found top-left segment: {top_left_segment}")
                # middle_segment = middle_bottom_segs.difference(top_left_segment)
                bottom_segment = middle_bottom_segs.difference(left_top_middle_segs)
                # print(f"Found bottom segment: {bottom_segment}")
                middle_segment = middle_bottom_segs.difference(bottom_segment)
                # print(f"Found middle segment: {middle_segment}")
    # top_left_char = ''
    # middle_char = ''
    # bottom_char = ''
    # for char in top_left_segment:
    #     top_left_char = char
    # for char in middle_segment:
    #     middle_char = char
    # for char in bottom_segment:
    #     bottom_char = char
    # print(f"Returning top-left {top_left_char}, middle {middle_char}, and bottom {bottom_char}")
    # return top_left_char, middle_char, bottom_char
    return top_left_segment, middle_segment, bottom_segment


def find_bottomleft_bottomright_topright_segments(pattern_lst, right_segs, top_seg, top_left_seg, middle_seg,
                                                  bottom_seg):
    # print(f"RIGHT SEGMENTS ARE HERE: {right_segs}")
    top_right_segment = ''
    bottom_left_segment = ''
    bottom_right_segment = ''
    for p in pattern_lst:
        if len(p) == 6:
            # print(f" For {p}")
            if len(set(p) & ((set(p)&top_seg)|(set(p)&top_left_seg)|(set(p)&middle_seg)|(set(p)&bottom_seg))) == 4 and len((set(p) & right_segs)) == 1:
                # print(f"For {p}")
            # if (middle_seg in p and top_seg in p and bottom_seg in p and top_left_seg in p and
            #         top_left_seg in p and right_segs not in p):
            #     b_left_b_right_segs = (set(top_seg) | set(top_left_seg) | set(middle_seg) | set(bottom_seg) | set(p)) - \
            #                           (set(top_seg) & set(top_left_seg) & set(middle_seg) & set(bottom_seg) & set(p))
                b_left_b_right_segs = set(p) - ((set(p)&top_seg)|(set(p)&top_left_seg)|(set(p)&middle_seg)|(set(p)&bottom_seg))
                # print(f"Found bottom-left and bottom-right segments: {b_left_b_right_segs}")
                bottom_left_segment = b_left_b_right_segs.difference(right_segs)
                # print(f"Found bottom-left segment: {bottom_left_segment}")
                bottom_right_segment = b_left_b_right_segs.difference(bottom_left_segment)
                # print(f"Found bottom-right segment: {bottom_right_segment}")
                top_right_segment = (set(right_segs)).difference(bottom_right_segment)
                # print(f"Found top-right segment: {top_right_segment}")

    # top_right_char = ''
    # bottom_left_char = ''
    # bottom_right_char = ''
    #
    # for char in top_right_segment:
    #     top_right_char = char
    # for char in bottom_left_segment:
    #     bottom_left_char = char
    # for char in bottom_right_segment:
    #     bottom_right_char = char
    # print(f"Returning top-right {top_right_char}, bottom-left {bottom_left_char}, and bottom-right {bottom_right_char}")
    # return top_right_char, bottom_left_char, bottom_right_char
    return top_right_segment, bottom_left_segment, bottom_right_segment


def get_number(segment_dict, index, values_array):
    num = ''
    #for values[i] in output_values:
        # print(f"VALUES TIME")
        # print(values)
    # print(f"OUTPUT VALUES: {values_array[index]}")
    for value in values_array[index]:
        # print(f"VALUE IS: {value}")
        #for j in range(0, len(value)):
        # print(f"Looking at value: {value}")
        digit = ''
        if len(value) == 2:
            digit = '1'
        elif len(value) == 3:
            digit = '7'
        elif len(value) == 4:
            digit = '4'
        elif len(value) == 7:
            digit = '8'
        elif len(value) == 5:
            if segment_dict['bottom_left'] in value:
                digit = '2'
            elif segment_dict['top_left'] in value:
                digit = '5'
            else:
                digit = '3'
        elif len(value) == 6:
            if segment_dict['middle'] in value and segment_dict['bottom_left'] not in value:
                digit = '9'
            elif segment_dict['middle'] in value and segment_dict['bottom_left'] in value:
                digit = '6'
            else:
                digit = '0'
            # print(f"DIGIT: {digit}")
        num = num + digit
        # print(f"NUM: {num}")
    return int(num)


signal_patterns = [patterns.split(' | ')[0].split(' ') for patterns in puzzle_input]
output_values = [values.split(' | ')[1].split(' ') for values in puzzle_input]

total_sum = 0
for i in range(0, len(signal_patterns)):
    signal_dict = {'top': '', 'top_right': '', 'middle': '',
                   'bottom_right': '', 'bottom': '', 'bottom_left': '',
                   'top_left': ''}

    # print(f"NEW DICT: {signal_dict}")
    # for pattern in signal_patterns[i]:
    # print(f"Check pattern: {signal_patterns[i]}")
    right_segs = find_right_segments(signal_patterns[i])
    top_seg = find_top_segment(signal_patterns[i], right_segs)
    left_top_middle_segs = find_lefttopmiddle_segments(signal_patterns[i], right_segs)
    top_left_seg, middle_seg, bottom_seg = find_topleft_middle_bottom_segments(signal_patterns[i], right_segs, top_seg,
                                                                               left_top_middle_segs)
    top_right_seg, bottom_left_seg, bottom_right_seg = find_bottomleft_bottomright_topright_segments(signal_patterns[i],
                                                                                                     right_segs,
                                                                                                     top_seg,
                                                                                                     top_left_seg,
                                                                                                     middle_seg,
                                                                                                     bottom_seg)
    signal_dict['top'] = ''.join(top_seg)
    signal_dict['top_right'] = ''.join(top_right_seg)
    signal_dict['middle'] = ''.join(middle_seg)
    signal_dict['bottom_right'] = ''.join(bottom_right_seg)
    signal_dict['bottom'] = ''.join(bottom_seg)
    signal_dict['bottom_left'] = ''.join(bottom_left_seg)
    signal_dict['top_left'] = ''.join(top_left_seg)

    # print(signal_dict)

    sum_values = 0
    # print(f"NEW SUM: {sum_values}")
    sum_values += get_number(signal_dict, i, output_values)
    # print(f"SUM VALUES: {sum_values}")
    total_sum += sum_values

print(total_sum)


