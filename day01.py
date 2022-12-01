# Day one of the advent of code challenge

data_file = 'day01_input.txt'

# Part one - find the largest amount of calories in list

one_elf_calories = 0
all_elf_calories = []
with open(data_file) as f:
    all_calories = f.readlines()
    for calorie in all_calories:
        try:
            one_elf_calories += int(calorie)
        except:
            all_elf_calories.append(one_elf_calories)
            one_elf_calories = 0

maximum_elf_calories = max(all_elf_calories)
print('Maximum number of calories = {}'.format(maximum_elf_calories))

# Part two - total number of calories the top three elves are carrying

all_elf_calories.sort(reverse = True)
total_top_3 = sum(all_elf_calories[:3])
print('Total number of calories carried by top three = {}'.format(total_top_3))
