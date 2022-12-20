import random


def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)


def main():
    player1 = input('Player 1, enter your name: ')
    player2 = input('Player 2, enter your name: ')

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1 + ' rolled ' + str(roll1))
    print(player2 + ' rolled ' + str(roll2))

    if roll1 > roll2:
        print(player1 + ' wins!')
    elif roll2 > roll1:
        print(player2 + ' wins!')
    else:
        print('Draw!')


main()
