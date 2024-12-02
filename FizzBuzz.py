import random

def main():
    random_number = random.randint(1, 100)
    user_guess = int(input("Guess a number between 1 and 100: "))
    while user_guess != random_number:
        if user_guess < random_number:
            print("Too low!")
        else:
            print("Too high!")
        user_guess = int(input("Guess again: "))
   
    print("You guessed correctly!")
def fizz_buzz():
    for i in range(100):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    # main()
    fizz_buzz()