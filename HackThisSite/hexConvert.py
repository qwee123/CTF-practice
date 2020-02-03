import sys

input = sys.argv[1]
input = input.split(',')
for hex in input:
    decode = chr(int(hex))
    print(decode, end='')