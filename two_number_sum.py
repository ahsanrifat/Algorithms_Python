input_list = [5, 6, 2, 8, 9, 3, 7, 1]
target_sum = 10


def solve_two_num_sum1(input_list, target_sum):
    mapping_dict = dict()
    for i in input_list:
        expected_num = target_sum - i
        if expected_num in mapping_dict:
            print(i, expected_num)
        else:
            mapping_dict[i] = None


def solve_two_num_sum2(input_list, target_sum):
    left_pointer = 0
    right_pointer = len(input_list) - 1
    input_list.sort()
    while left_pointer != right_pointer:
        current_sum = input_list[left_pointer] + input_list[right_pointer]
        if current_sum == target_sum:
            print(input_list[left_pointer], input_list[right_pointer])
            right_pointer -= 1
            left_pointer += 1
        elif current_sum > target_sum:
            right_pointer -= 1
        else:
            left_pointer += 1


solve_two_num_sum2(input_list, target_sum)