# Day 14 #

# Higher Lower Game Project

import higherLowerGame
import random
import os

data = higherLowerGame.data[:]
vs = higherLowerGame.vs
logo = higherLowerGame.logo

def pick_random_influencer():
    influencer_index = random.randint(0, len(data) - 1)
    return influencer_index

def getting_influencer_data(influencer_index):
    target = data[influencer_index]
    name = target["name"]
    follower_count = target["follower_count"]
    description = target["description"]
    country = target["country"]
    return name, follower_count, description, country

def calculate_followers(first_influ_followers, second_influ_followers, user_input):
    global Final_score
    is_right = False
    os.system("cls")
    print(logo)
    # if first_influ_followers > second_influ_followers:
    #     if user_input == "a":
    #         Final_score += 1
    #         print(f"You're right! Current score: {Final_score}.")
    #         return True
    #     elif user_input == "b":
    #         print(f"Sorry, that's wrong. Final score: {Final_score}")
    #         return False
    # elif first_influ_followers < second_influ_followers:
    #     if user_input == "b":
    #         Final_score += 1
    #         print(f"You're right! Current score: {Final_score}.")
    #         return True
    #     elif user_input == "a":
    #         print(f"Sorry, that's wrong. Final score: {Final_score}")
    #         return False
    if first_influ_followers > second_influ_followers:
        is_right = user_input == "a" # will return true if user input == a and 1st > 2nd
    else:
        is_right = user_input == "b" # will return true if user input == b and 1st < 2nd
    if is_right:
        Final_score += 1
        print(f"You're right! Current score: {Final_score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {Final_score}")

    return is_right

def higherLower():
    global Final_score
    global next_round_influ_index
    Final_score = 0
    while True:
        if Final_score > 0:
            first_influ_num = next_round_influ_index
        else:
            first_influ_num = pick_random_influencer()

        first_influ_name, first_influ_followers, first_influ_description, first_influ_country = getting_influencer_data(first_influ_num)
        print(f"Compare A: {first_influ_name}, a {first_influ_description}, from {first_influ_country}")

        print(vs)
        second_influ_num = pick_random_influencer()
        while first_influ_num == second_influ_num:
            second_influ_num = pick_random_influencer()
        next_round_influ_index = second_influ_num
        second_influ_name, second_influ_followers, second_influ_description, second_influ_country = getting_influencer_data(second_influ_num)
        print(f"Against B: {second_influ_name}, a {second_influ_description}, from {second_influ_country}")
        user_input = input("Who has more followers? Type 'A' or 'B':   ").lower()
        if not calculate_followers(first_influ_followers, second_influ_followers, user_input):
            user_choice = input("Do you want to play again? Type 'Y' for yes and 'N' for no:  ").lower()
            if  user_choice == 'y':
                os.system("cls")
                print(logo)
                higherLower()
                break
            else:
                break
            
Final_score = 0
next_round_influ_index = ""
print(logo)
higherLower()
    
