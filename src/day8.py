import operator
import re
import sys

input = sys.stdin.read().splitlines()

pattern = re.compile(r'^(\w+) (\w{3}) (-?\d+) if (\w+) (.{1,2}) (-?\d+)$')
ops = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
}

registers = {}
max_v = 0
for line in input:
    reg, op, v, con_reg, con_op, con_v = pattern.match(line).groups()

    v = int(v)
    con_v = int(con_v)

    reg_v = registers.get(reg) if reg in registers else 0
    con_reg_v = registers.get(con_reg) if con_reg in registers else 0

    max_v = max(max_v, reg_v)

    if ops[con_op](con_reg_v, con_v):
        registers[reg] = reg_v + v if op == 'inc' else reg_v - v

print('Part 1:', max(registers.values()))
print('Part 2:', max_v)
