import sys

input = sys.stdin.read().splitlines()

count = 0
for line in input:
    words = line.split()
    if len(set(words)) == len(words):
        count += 1

print('Part 1:', count)

count = 0
for line in input:
    used = []
    words = line.split()
    for word in words:
        letters = list(word)
        letters.sort()
        used.append(''.join(letters))
    if len(set(used)) == len(words):
        count += 1

print('Part 2:', count)
