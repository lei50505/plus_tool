#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''doc'''

def get_by_sum(src_arr, tar_sum):
    '''doc'''
    src_arr = sorted(src_arr, key=lambda item: item["key"])
    final_result = []
    cur_result = []
    def iter_by_sum(cur_sum, cur_index):
        '''doc'''
        if cur_index >= len(src_arr):
            return
        cur_val = src_arr[cur_index]["key"]
        if cur_sum < cur_val:
            return
        if cur_sum == cur_val:
            tmp = []
            tmp.append(src_arr[cur_index]["data"])

            for cur_result_item in cur_result:
                tmp.append(src_arr[cur_result_item]["data"])
            final_result.append(tmp)

        cur_result.append(cur_index)
        iter_by_sum(cur_sum - cur_val, cur_index + 1)
        cur_result.pop()
        iter_by_sum(cur_sum, cur_index + 1)

    iter_by_sum(tar_sum, 0)
    return final_result


def main():
    '''doc'''
    src_arr = [{"key":1, "data":"dasdsa1"}, {"key":5, "data":"2"}, {"key":4, "data":"3"}]
    tar_arr = get_by_sum(src_arr, 5)
    print(tar_arr)


if __name__ == "__main__":
    main()
