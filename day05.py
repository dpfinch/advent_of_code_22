# Day five of the advent of code challenge

data_file = 'data_input/day05_input.txt'

# Part one - Find which crate is ontop of each stack

stack_lines = []
instructions = []

open_file = open(data_file)
while True:
    file_line = open_file.readline()
    # pdb.set_trace()
    if not file_line:
        break
    if file_line.startswith('move'):
        instructions.append(file_line.strip('\n'))
    elif file_line.startswith('['):
        stack_lines.append(file_line.strip('\n'))
    else:
        continue
    
open_file.close()
stacks = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
for stack_line in stack_lines:
    for n,x in enumerate(range(0,35,4)):
        crate = stack_line[x:x+4].strip()
        try:
            crate = crate[1] # Get the letter from middle of brackets
            stacks[n+1].append(crate)
        except IndexError:
            continue

for instruction in instructions:
    instr_split = instruction.split()
    amount = int(instr_split[1])
    from_stack = int(instr_split[3])
    to_stack = int(instr_split[5])

    for move in range(amount):
        crate_letter = stacks[from_stack].pop(0)
        stacks[to_stack].insert(0,crate_letter)
        
top_crates = ''.join([stacks[x][0]for x in stacks.keys()])
print('Arrangement of top crates = {}'.format(top_crates))

# Part two - Same as above but move all together, not one at a time

stacks = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
for stack_line in stack_lines:
    for n,x in enumerate(range(0,35,4)):
        crate = stack_line[x:x+4].strip()
        try:
            crate = crate[1] # Get the letter from middle of brackets
            stacks[n+1].append(crate)
        except IndexError:
            continue

for instruction in instructions:
    instr_split = instruction.split()
    amount = int(instr_split[1])
    from_stack = int(instr_split[3])
    to_stack = int(instr_split[5])

    crate_letters = stacks[from_stack][:amount]
    del stacks[from_stack][:amount]
    stacks[to_stack] = crate_letters + stacks[to_stack]

        
top_crates = ''.join([stacks[x][0]for x in stacks.keys()])
print('New arrangement of top crates = {}'.format(top_crates))
