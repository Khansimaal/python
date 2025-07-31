import random, sys

print('Rock, Paper, Scissors')

# Trackers
wins = 0
losses = 0
ties = 0

# Ask play or quit once at the start
print('Play (p) or Quit (q)')
decision = input().lower()
if decision == 'q':
    sys.exit()
if decision != 'p':
    print('Invalid input! Exiting.')
    sys.exit()

while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    # Get and display player's choice
    print('Type r for rock, p for paper, s for scissors, or q to quit')
    playermove = input().lower()
    if playermove == 'q':
        sys.exit()
    if playermove not in ['r', 'p', 's']:
        print('Invalid move! Type r, p, s, or q.')
        continue
    if playermove == 'r':
        print('rock vs...')
    elif playermove == 'p':
        print('paper vs...')
    elif playermove == 's':
        print('scissors vs...')

    # Display computer's choice
    random_num = random.randint(1, 3)
    if random_num == 1:
        computer_move = 'r'
        print('rock')
    elif random_num == 2:
        computer_move = 'p'
        print('paper')
    elif random_num == 3:
        computer_move = 's'
        print('scissors')

    # Record outcome
    if playermove == computer_move:
        print("It's a tie baby")
        ties += 1
    elif (playermove == 'r' and computer_move == 's') or \
         (playermove == 'p' and computer_move == 'r') or \
         (playermove == 's' and computer_move == 'p'):
        print("You win bruh")
        wins += 1
    else:
        print("I win bruh")
        losses += 1
