import art
import random
from game_data import data

# Válasszon ki tetszőlegesen egy személyt a game_data["data"]-ból, ami még nem volt (lista azokról, akik már voltak)

already_picked = []
player_score = 0

def select_person(chosen_people, profile_data):
    selected = random.choice(profile_data)
    while selected in chosen_people:
        selected = random.choice(profile_data)
    already_picked.append(selected)
    return selected

# Dictionary, amiben az aktuális person-okat gyűjtjük

current = {
    "A": select_person(already_picked, data),
    "B": select_person(already_picked, data)
}

# function, ami ellenőrzi, hogy a felhasználó jól tippelte meg, hogy a "B" followerje lower/higher az A person followerjétől

def check_follower_count(current_persons):
    if current_persons["A"]["follower_count"] > current_persons["B"]["follower_count"]:
        return "A"
    elif current_persons["A"]["follower_count"] < current_persons["B"]["follower_count"]:
        return "B"
    else:
        return "draw"

def check_user_guess(current_persons, user_guess):
    result = check_follower_count(current_persons)
    if result == user_guess:
        if result == "A":
            current["B"] = select_person(already_picked, data)
        else:
            current["A"] = current["B"]
            current["B"] = select_person(already_picked, data)
        return True
    elif result == "draw":
        current["B"] = select_person(already_picked, data)
        return "draw"
    elif result == 'A' and user_guess == 'B' or result == 'B' and user_guess == 'A':
        return False
    else:
        print("Wrong input!")
        return "wrong input"

def game(score):
    print(art.logo)
    while True:
        print(f"\n Compare A: {current['A']['name']}, {current['A']['description']} from {current['A']['country']}")
        print(art.vs)
        print(f"\n Compare B: {current['B']['name']}, {current['B']['description']} from {current['B']['country']}")

        user_input = input("Who has more followers? Type 'A' or 'B': ")
        result = check_user_guess(current, user_input)
        if result == "draw" or result == "wrong input":
            continue
        elif result:
            score += 1
            print(f"Yeah, you win! Your score: {score}")
        else:
            print(f"You lost! Your final score: {score}")
            break

game(player_score)
