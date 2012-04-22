# http://codeforces.ru/problemset/problem/145/D

import sys

arrSize = int(sys.stdin.readline())
arr = sys.stdin.readline().split()

def isHappy(num):
    for digit in num:
        if not digit == '4' or not digit == '7':
            return False
    return True

happyNums = {}

pos = 0
for num in arr:
    if isHappy(num):
        if num not in happyNums:
            happyNums[num] = []
        happyNums[num].append(pos)
    pos += 1