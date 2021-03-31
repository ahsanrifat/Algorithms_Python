input_list = [5, 6, 2, 8, 9, 3, 7, 1]
target_sum = 10

mapping_dict = dict()
# result_pair_dict = dict()
for i in input_list:
    mapping_dict[i] = ""
for i in input_list:
    expected_num = target_sum - i
    if expected_num in mapping_dict:
        print(i, expected_num)
        del mapping_dict[i]