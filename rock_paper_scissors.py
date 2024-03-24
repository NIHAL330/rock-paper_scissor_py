import random
print()
print(' ◜                                     ◝   ')
print('                  PLAY                         ')
print('       ⊱ ROCK - PAPER - SCISSORS ⊰     ')
print(' ◟                                     ◞  ')

start = ('ROCK','PAPER','SCISSORS')
running = True
while running:
    play = None
    computer = random.choice(start)

    while play not in start:
        print()
        play = input("ENTER YOUR CHOICE:")
        print()
        play=play.upper()
    print(f'YOU: {play}')
    print()
    print(f'COMPUTER: {computer}')
    print()
    if play==computer:
        print("⁕ IT'S DRAW‼ ⁕")
        print()
    elif play=="Rock" and computer=='Scissors':
        print("⁕ YOU WIN ⁕")
        print()
    elif play=='Scissors' and computer=='Paper':
        print('⁕ YOU WIN ⁕')
        print()
    elif play=='Paper' and  computer=='Rock':
        print('⁕ YOU WIN ⁕')
        print()
    else:
        print('⁕ YOU LOSS ⁕')
        print()
    if not input('PLAY AGAIN (Y/N):').lower()=='y':
        print()
        running=False
print('⊱ THANKS FOR PLAYING ⊰')
