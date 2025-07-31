#this is a guess the number game
import random
secretnumber = random.randint(1, 10)
print('ive thought of a number between 1 and 10')

#ask the player for a max of 6 times to guess
for guessing in range(1, 7):
    print('')
    print('Alright take a guess')
    guess = int(input())


    if guess > secretnumber:
        print("that's higher than what i thought bruh")
    elif guess < secretnumber:
       print("that's lower than the number i thought")
    else:
        break

if guess == secretnumber:
    print('you got it babyyy!')
else :
        print('---------------------')
        print('man you are pretty dumb ' + str(secretnumber) + ' this was the numberrrrrrrrrr')
