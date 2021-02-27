# Display art
from art import logo,vs
from game_data import data
import random
#Generate a random data from game data
import os
clear = lambda: os.system('cls')
print(logo)

def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess,a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Compare B:{format_data(account_b)}")
    guess = input('who has more followers? Type "A" or "B": ').lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct =check_answer(guess, a_follower_count,b_follower_count)

    clear()
    if is_correct:
        score +=1
        print(f"You are right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"sorry, that's wrong. Final score: {score}")

