# Guessing Game

secret_number = 8
Guess_Count =0
Guess_Limit = 3
while Guess_Count<Guess_Limit:
    guess = int(input("Guess: "))
    Guess_Count+=1
    if guess == secret_number:
        print("You Won")
        break
else:
    print("You Failed")
