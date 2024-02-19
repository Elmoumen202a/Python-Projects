import random
from IPython.display import clear_output

def num_dice():
    while True:
        try:
            num = int(input('Enter the number of dice (1 or 2): '))
            if num not in [1, 2]:
                raise ValueError('Please enter 1 or 2 only')
            else:
                return num
        except ValueError as err:
            print(err)

def roll_dice(num):
    min_val, max_val = 1, 6

    clear_output(wait=True)

    if num == 1:
        print('Rolling the die...')
        result = random.randint(min_val, max_val)
        print(f'The value is: {result}')
    elif num == 2:
        print('Rolling the dice...')
        dice_1 = random.randint(min_val, max_val)
        dice_2 = random.randint(min_val, max_val)
        total = dice_1 + dice_2
        print(f'The values are:\nDice One: {dice_1}\nDice Two: {dice_2}\nTotal: {total}')

if __name__ == '__main__':
    while True:
        num = num_dice()
        roll_dice(num)

        roll_again = input('Roll again? (yes/no): ')
        if roll_again.lower() not in ['yes', 'y']:
            break
