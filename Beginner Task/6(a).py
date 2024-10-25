import random
def roll_dice_simulation():
    num_rolls = 20  
    rolls = []  
    for _ in range(num_rolls):
        roll = random.randint(1, 6) 
        rolls.append(roll) 
    count_6 = rolls.count(6) 
    count_1 = rolls.count(1)  
    count_double_6 = sum(1 for i in range(1, len(rolls)) if rolls[i] == 6 and rolls[i-1] == 6)  
    print(f"Rolls: {rolls}")
    print(f"Number of times you rolled a 6: {count_6}")
    print(f"Number of times you rolled a 1: {count_1}")
    print(f"Number of times you rolled two 6s in a row: {count_double_6}")
roll_dice_simulation()