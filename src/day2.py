import sys

input = sys.stdin.read().splitlines()

res = 0
for line in input:
    numbers = list(map(int, line.split()))
    res += max(numbers) - min(numbers)
print('Part 1:', res)

res = 0
for line in input:
    numbers = list(map(int, line.split()))
    for i1, n1 in enumerate(numbers):
        for n2 in numbers[i1 + 1:]:
            if n2 % n1 == 0:
                res += n2 // n1
            if n1 % n2 == 0:
                res += n1 // n2
print('Part 2:', res)
