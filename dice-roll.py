import random

def rolldice(min, max):
    while True:
        print("press enter to roll a dice")
        number = random.randint(min, max)
        print(f"your dice is {number}")
        question = input("would you like to rolldice again? (y/n): ").lower()
        if question == "n":
            break

rolldice(1, 6)