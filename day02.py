# Day two of the advent of code challenge
import pdb
data_file = 'data_input/day02_input.txt'

# Part one - Rock paper scissors competition point total
# Player 1
# A = Rock
# B = Paper
# C = Scissors

# Player 2
# X = Rock -> 1 point
# Y = Paper -> 2 points
# Z = Scissors -> 3 points

# Loose 0 points, draw 3 points, win 6 points
draw_combos = [['A','X'],['B','Y'],['C','Z']]
I_win_combos = [['A','Y'],['B','Z'],['C','X']]
elf_win_combos = [['A','Z'],['B','X'],['C','Y']]

point_dict = {'X':1, 'Y':2, 'Z':3}

with open(data_file) as f:
    rps_results = f.readlines()

score_total = 0
for line in rps_results:
    result = line.split()
    score_total += point_dict[result[1]]
    if result in draw_combos:
        score_total += 3
    if result in I_win_combos:
        score_total += 6
    
print('Total of my score = {}'.format(score_total))   

# Part two - what I need to play to win/loose/draw

# Player 2
# X = lose 
# Y = draw 
# Z = win 
# Points I'll get with what I need to play (i.e. they play rock, I must play paper which is 2 points)
win_dict = {'A': 2, 'B': 3, 'C': 1}
lose_dict = {'A': 3, 'B': 1, 'C': 2}
draw_dict = {'A': 1, 'B': 2, 'C': 3}

score_total = 0
for line in rps_results:
    result = line.split()
    if result[1] == 'X': # Lose
        score_total += lose_dict[result[0]]
    if result[1] == 'Y': # Draw
        score_total += draw_dict[result[0]] + 3
    if result[1] == 'Z': # Win
        score_total += win_dict[result[0]] + 6


print('My new score total = {}'.format(score_total))