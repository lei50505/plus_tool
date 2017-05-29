#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''doc'''

def get_num_in_arr(arr, add_sum):
    '''doc'''
    arr_len = len(arr)
    bin_max = 1<<arr_len
    result_arr = []
    for bin_num in range(1, bin_max):
        cur_sum = 0
        index_arr = []
        for bin_index in range(arr_len):
            if bin_num & (1<<bin_index) != 0:
                cur_sum += arr[bin_index]
                index_arr.append(bin_index)

        if add_sum == cur_sum:
            result_arr.append(index_arr)

    return result_arr

if __name__ == "__main__":
    ARR = [1, 2, 3, 4, 5]
    NUM = 12
    print(get_num_in_arr(ARR, NUM))
