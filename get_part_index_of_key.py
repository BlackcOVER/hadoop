'''
  确认key在MR任务结果的哪一个part中
'''

import sys
import argparse

# sys.maxsize = 2147483647

parser = argparse.ArgumentParser()
parser.add_argument('--key', type=str, default='')
parser.add_argument('--nums_part', type=int, default=100)
args, _ = parser.parse_known_args()

uid = bytearray(args.key.encode())
length = len(uid)
hash_ = 1
for i in range(length):
    hash_ = (31 * hash_) + uid[i]
part_index = (hash_ & sys.maxsize) % args.nums_part
print(part_index)
