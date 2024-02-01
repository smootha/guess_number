from random import randint

number = randint(1, 100)
print("Guess the number between 1 and 100")

while True:
    guess = int(input("Enter your number: "))

    if guess > number:
        print("Your number is more")
    elif guess < number:
        print("Your number is less")
    elif guess == number:
        break

print("Good job!!!")
