# -*- coding: utf-8 -*-

import random


# 生成指定长度的0-9串
def key_gen(key_len):
    key_list = [random.choice("0123456789abcdefghijklmnopqrstuvwxyz") for i in range(key_len)]
    return "".join(key_list)
