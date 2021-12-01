import random

name = input("Enter your name: ")
print(f"Hello, {name}")
print()
options_string = input()

if options_string == "":
    options = ["rock", "paper", "scissors"]
else:
    options = options_string.split(",")

print("Okay, let's start")

rating_dict = {}
with open("rating.txt", "r") as finput:
    for line in finput.readlines():
        words = line.split()
        rating_dict[words[0]] = int(words[1])

if name in rating_dict:
    player_rating = rating_dict[name]
else:
    player_rating = 0

while True:
    player_answer = input()

    if player_answer == "!exit":
        print("Bye!")
        exit()

    if player_answer == "!rating":
        print(f"Your rating: {player_rating}")
        continue

    if player_answer not in options:
        print("Invalid input")
        continue

    answer_index = options.index(player_answer)
    new_list = options[answer_index + 1:] + options[0:answer_index]

    computer_answer = random.choice(options)

    if computer_answer == player_answer:
        print(f"There is a draw ({computer_answer})")
        player_rating += 50
    elif new_list.index(computer_answer) < len(new_list) // 2:
        print(f"Sorry, but the computer chose {computer_answer}")
    else:
        print(f"Well done. The computer chose {computer_answer} and failed")
        player_rating += 100