# Day four of the advent of code challenge
data_file = 'data_input/day04_input.txt'

# Part one - 

with open(data_file) as f:
    assignment_pairs = f.readlines()

overlap_total = 0

for pair in assignment_pairs:
    first_lot = pair.split(',')[0]
    second_lot = pair.split(',')[1]
    first_start = int(first_lot.split('-')[0])
    first_end = int(first_lot.split('-')[1])
    second_start = int(second_lot.split('-')[0])
    second_end = int(second_lot.split('-')[1])
    set_a = set(range(first_start, first_end + 1))
    set_b = set(range(second_start, second_end + 1))
    if set_a.issubset(set_b) or set_b.issubset(set_a):
        overlap_total += 1
print('Number of overlapping assignments = {}'.format(overlap_total))


# Part two - How many assignment pairs overlap at all
overlap_total = 0
for pair in assignment_pairs:
    first_lot = pair.split(',')[0]
    second_lot = pair.split(',')[1]
    first_start = int(first_lot.split('-')[0])
    first_end = int(first_lot.split('-')[1])
    second_start = int(second_lot.split('-')[0])
    second_end = int(second_lot.split('-')[1])
    set_a = set(range(first_start, first_end + 1))
    set_b = set(range(second_start, second_end + 1))
    if len(set_a.intersection(set_b)) > 0:
        overlap_total += 1

print('Number of overlapping pairs = {}'.format(overlap_total))
