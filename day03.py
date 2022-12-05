# Day three of the advent of code challenge
import string
data_file = 'data_input/day03_input.txt'

# Part one - Find the sum of items in the rucksack

with open(data_file) as f:
    rucksack_list = f.readlines()

total_sum = 0
for rucksack in rucksack_list:
    half_num_items = int(len(rucksack.strip())/2)
    items_1 = rucksack.strip()[:half_num_items]
    items_2 = rucksack.strip()[half_num_items:]
    in_both = set(items_1) & set(items_2)

    for letter in in_both:
        if letter in string.lowercase:

            point = string.lowercase.index(letter) + 1
        else:
            point = string.uppercase.index(letter) + 27
        total_sum += point

print('Total sum for the priority items in rucksacks = {}'.format(total_sum))

# Part two - find common item between groups of three elves(lines)
grouped_threes = zip(*[iter(rucksack_list)] * 3)

total_sum = 0
for group in grouped_threes:

    items_1 = group[0].strip()
    items_2 = group[1].strip()
    items_3 = group[2].strip()

    in_all = set(items_1) & set(items_2) & set(items_3)

    for letter in in_all:
        if letter in string.lowercase:

            point = string.lowercase.index(letter) + 1
        else:
            point = string.uppercase.index(letter) + 27
        total_sum += point
print('Total of unique items in group = {}'.format(total_sum))