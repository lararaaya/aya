import random
# Generate a random number between 1 and 100
number = random.randint(1, 100)
print("welcom to the guess the number game")
print("i'm thinking of a number between 1 and 100. can you guess wath it is?")
guess = int(input("entrer your guess: "))
while guess !=number:
    if guess > number:
        print("your guess is too high. guess again.")
    else:
        print("your guess is too low. guess again.") 
    guess = int(input("enter your guesse:"))   
print("congratulation! you guessed the number!")        