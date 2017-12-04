import sys

input = sys.stdin.readline().strip()
chars_c = len(input)

res = sum(int(c) for i, c in enumerate(input) if c == input[(i + 1) % chars_c])
print('Part 1:', res)

distance = chars_c // 2
res = sum(int(c) for i, c in enumerate(input) if c == input[(i + distance) % chars_c])
print('Part 2:', res)
