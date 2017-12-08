import re
import sys

input = sys.stdin.read().splitlines()

pattern = re.compile(r'^(\w+) \((\d+)\)( -> )?(.+)?$')

programs = {}
weights = {}
total_children = []
for line in input:
    name, weight, _, children = pattern.match(line).groups()

    children = [c.strip() for c in children.split(',')] if children is not None else []

    programs[name] = children
    total_children.extend(children)
    weights[name] = int(weight)

root = set(programs.keys()).difference(total_children).pop()
print('Part 1:', root)


def check_weight(node):
    total_weight = weights[node]

    t_weights = {}
    for child in programs[node]:
        tower_weight = check_weight(child)
        total_weight += tower_weight

        # Store children weights to find the incorrect one later.
        if tower_weight not in t_weights:
            t_weights[tower_weight] = []
        t_weights[tower_weight].append(child)

    # If weights don't match, we found the children with incorrect weight.
    if len(t_weights) > 1:
        correct_w = max(t_weights, key=(lambda k: len(t_weights[k])))
        incorrect_w = min(t_weights, key=(lambda k: len(t_weights[k])))

        print('Part 2:', weights[t_weights[incorrect_w][0]] - (incorrect_w - correct_w))
        exit()

    return total_weight


check_weight(root)
