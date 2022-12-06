# Day six of the advent of code challenge
data_file = 'data_input/day06_input.txt'

# Part one - How many characeters need to be processed before the first start of packet marker is deteced?

with open(data_file) as in_file:
    characters = in_file.readline()

position = 3

for x in range(len(characters)):
    packet = characters[x:x+4]
    position += 1
    if len(set(packet)) == 4:
        break

print('First start-of-packet marker = {}'.format(position))
# Part two - same as above but looking for distinct makers of 14 characters, not 4

position = 13

for x in range(len(characters)):
    packet = characters[x:x+14]
    position += 1
    if len(set(packet)) == 14:
        break
 
print('First start-of-message marker = {}'.format(position))
