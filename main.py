# -*- coding: utf-8 -*-

import timeit
from bloom_filter.lib.bloom_filter import BloomFilter
from bloom_filter.utils.utils import key_gen

STRING_COUNT = 100000
STRING_LEN = 10
bloom_filter = BloomFilter(1000000000, 5)


def check():
    sth_list = [key_gen(STRING_LEN) for i in range(STRING_COUNT)]
    for sth in sth_list:
        bloom_filter.add(sth)

    sth_list1 = sth_list.copy()
    sth_list1.append(key_gen(STRING_LEN))
    sth_list1.append(key_gen(STRING_LEN))
    sth_list1.append(key_gen(STRING_LEN))

    for sth in sth_list1:
        contain = sth in bloom_filter
        # if contain:
        #     print('{} is in bloom_filter'.format(sth))
        # else:
        #     print('{} is not in bloom_filter'.format(sth))

if __name__ == '__main__':
    t = timeit.Timer(stmt=check)
    print('[consume time: {}]'.format(t.timeit(1)))

