import random

print('This is a number guessing game!')

def check(g):
    if g <= 100:
        if g >= 1:
            valid=True
        else:
            valid=False
    else:
        valid=False
    return valid

def play():
    print("I am thinking of a number between 1 and 100")
    print("If you can guess it in 5 tries or less, you win!")
    num=random.randint(1,100)
    guess = int(raw_input('Make your first guess:  '))
    count=1
    left=4
    win=False
    for guess_count in range(0,4):
        while check(guess)==False:
            guess=int(raw_input("That number isn't between 1 and 100! You're lucky I'm not counting that as a guess. Enter your guess:  "))
        if guess==num:
            print('You win! And in only ' + str(count) + ' guesses! The number was ' + str(num))
            win=True
            break
        elif guess<num:
            if left >1:
                print('That guess was too low! You have ' + str(left) + ' guesses remaining')
            if left==1:
                print('That guess was too low! You have ' + str(left) + ' guess remaining')
            left=left-1
            count=count+1
            guess=int(raw_input("Make your next guess: "))
        else:
            if left > 1:
                print('That guess was too high! You have ' + str(left) + ' guesses remaing')
            if left == 1:
                print('That guess was too high! You have ' + str(left) + ' guess remaing')
            left=left-1
            count=count+1
            guess=int(raw_input("Make your next guess: "))
    if guess==num:
        print('You win! And in only ' + str(count) + ' guesses! The number was ' + str(num))
        win=True
    if win==False:
        print('Sorry, you ran out of guesses!  I win! The correct number was ' + str(num))
    ask=raw_input('Would you like to play again? y for yes or n for no:  ')
    if ask=='y':
        play()
    elif ask!='n':
        ask==raw_input('Oops, that is not a valid choice, n to quit, y to keep playing:  ')
    else:
        print('Thanks for playing!')

play()
