# -*- coding: utf-8 -*-

import mmh3
from bitarray import bitarray


class BloomFilter(object):

    def __init__(self, size, hash_count):
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.size = size
        self.hash_count = hash_count

    def __len__(self):
        return self.bit_array.length()

    def add(self, item):
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    def __contains__(self, item):
        contain = True
        for i in range(self.hash_count):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] == 0:
                contain = False
                return contain
        return contain
