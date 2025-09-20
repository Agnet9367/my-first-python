import random 
print("Pick the level 1, 2. or 3: ")
level = int(input())
if level == 1:
    chances = 12
elif level == 2:
    chances = 9
elif level == 3:
    chances = 6
else:
    print("Invalid level")
    exit()
number = random.randint(1, 100)
print(" Since you picked level", level, "you have", chances, "chances to guess the number between 1 and 100")
for i in range(chances):
    guess = int(input("Make a guess: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("You got it! The answer was", number)
        break
else:             
    print("You've run out of guesses. The number was", number)                              