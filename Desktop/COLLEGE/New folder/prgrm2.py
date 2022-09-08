import random

wn = random.randint(0,100)

print(wn)
def guess(un):
    game_over = False
    guess_counter = 1
    while not game_over:
        if wn == un:
            print(f"YAY! in {guess_counter} {'time' if guess_counter==1 else 'times'}")
            game_over = True
        else:
            if un > wn:
                print(" < ")
            else:
                print(" > ")
            guess_counter += 1    
            un = int(input("Enter again: "))                
un = int(input("Enter a number: "))
guess(un)            