# Day 11 #

# The blackjack capstone project
import random
import os # to clear terminal using os.system('cls')
os.system('cls')
blackjack_logo = ''' 
.------.         _     _            _    _            _    
|A_  _ |        | |   | |          | |  (_)          | |   
|( \/ )|-----.  | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  / | /\  |  | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ A|/  \ |  | |_) | | (_| | (__|   <| | (_| | (__|   < 
`------'\  / |  |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                          _/ |   
      `------'                         |__/
'''
CARDS = ['''
 -------
|K      |
|       |
|       |
|       |
|      K|
 ------- ''', '''
 -------
|Q      |
|       |
|       |
|       |
|      Q|
 ------- ''', ''' 
 -------
|J      |
|       |
|       |
|       |
|      J|
 ------- ''', '''
 -------
|10     |
|       |
|       |
|       |
|     10|
 ------- ''', '''
 -------
|9      |
|       |
|       |
|       |
|      9|
 ------- ''', '''
 -------
|8      |
|       |
|       |
|       |
|      8|
 ------- ''', '''
 -------
|7      |
|       |
|       |
|       |
|      7|
 ------- ''', '''
 -------
|6      |
|       |
|       |
|       |
|      6|
 ------- ''', '''
 -------
|5      |
|       |
|       |
|       |
|      5|
 ------- ''', '''
 -------
|4      |
|       |
|       |
|       |
|      4|
 ------- ''', '''
 -------
|3      |
|       |
|       |
|       |
|      3|
 ------- ''', '''
 -------
|2      |
|       |
|       |
|       |
|      2|
 ------- ''', ''' 
 -------
|A      |
|       |
|       |
|       |
|      A|
 ------- '''
]
Blank_card = '''
 -------
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
|XXXXXXX|
 ------- '''

blackjack_cards = [
    {"card_name": "K", "card_value": 10},
    {"card_name": "Q", "card_value": 10},
    {"card_name": "J", "card_value": 10},
    {"card_name": "10", "card_value": 10},
    {"card_name": "9", "card_value": 9},
    {"card_name": "8", "card_value": 8},
    {"card_name": "7", "card_value": 7},
    {"card_name": "6", "card_value": 6},
    {"card_name": "5", "card_value": 5},
    {"card_name": "4", "card_value": 4},
    {"card_name": "3", "card_value": 3},
    {"card_name": "2", "card_value": 2},
    {"card_name": "A", "card_value": [1,11]}
]

def pick_a_card(number_of_cards, new_cards_list):
    for x in range(0, number_of_cards):
        random_number = random.randint(0, len(blackjack_cards) - 1)
        new_cards_list.append(blackjack_cards[random_number])
    return new_cards_list

def calculate_cards_value(cards_list):
    total_card_value = 0
    total_of_As = 0
    for item in cards_list:
        card = item["card_name"]
        if card == "A":
            total_of_As += 1
        else:
            value = item["card_value"]
            total_card_value += value
    if(total_of_As > 0):
        for A in range(0,total_of_As):
            if total_card_value <= 10:
                total_card_value += blackjack_cards[12]["card_value"][1] # 11
            else:
                total_card_value += blackjack_cards[12]["card_value"][0] # 1
    return total_card_value

def display_cards_value(cards_list):
    totalCardsValue = ""
    cards_names_list = []
    for card in cards_list:
        cards_names_list.append(card["card_name"])
    totalCardsValue = ", ".join(cards_names_list)
    return totalCardsValue

def check_winner(player_card_value, dealer_card_value, first_hand):
    game_status = ["blackjack", "win", "draw", "lose", "both lose"]
    current_status = ""
    if player_card_value == 21 and first_hand == True and dealer_card_value < 21:
        current_status = game_status[0]
        print("+-+-+-+-+-+-+-+")
        print("You Got A Blackjack!")
        print("+-+-+-+-+-+-+-+")
    elif player_card_value < 21 and first_hand == True and dealer_card_value == 21:
        current_status = game_status[3]
        print("+-+-+-+-+-+-+-+")
        print("Dealer Got A Blackjack!")
        print("+-+-+-+-+-+-+-+")
    elif (player_card_value > dealer_card_value and player_card_value <= 21) or (dealer_card_value > 21 and player_card_value <= 21):
        current_status = game_status[1]
        print("+-+-+-+-+-+-+-+")
        print("You Win!")
        print("+-+-+-+-+-+-+-+")
    elif player_card_value == dealer_card_value and player_card_value <= 21:
        current_status = game_status[2]
        print("+-+-+-+-+-+-+-+")
        print ("Not that luck after all, Draw!")        
        print("+-+-+-+-+-+-+-+")
    elif (player_card_value < dealer_card_value and dealer_card_value <= 21) or (player_card_value > 21 and dealer_card_value <= 21):
        current_status = game_status[3]
        print("+-+-+-+-+-+-+-+")
        print("You Lost!")
        print("+-+-+-+-+-+-+-+")
    else:
        current_status = game_status[4]
        print("+-+-+-+-+-+-+-+")
        print("Both Player and Dealer Lost!")
        print("+-+-+-+-+-+-+-+")
    return current_status

def show_cards_icons(cardsList, is_player_cards):
    iconsList = []
    iconsString = ""
    if is_player_cards:
        for card in cardsList:
            index_of_card = blackjack_cards.index(card)
            card_icon = CARDS[index_of_card]
            iconsList.append(card_icon)
    else:
        for index, card in enumerate(cardsList):
            if index == 0:
                index_of_card = blackjack_cards.index(card)
                card_icon = CARDS[index_of_card]
            else:
                card_icon = Blank_card
            iconsList.append(card_icon)
    iconsString = " ".join(iconsList)
    return iconsString

def game():
        player_card_value = 0
        dealer_card_value = 0
        player_cards = []
        dealer_cards =[]

        print(blackjack_logo)
        pick_a_card(2, player_cards)
        pick_a_card(2, dealer_cards)
        player_card_value = calculate_cards_value(player_cards)
        dealer_card_value = calculate_cards_value(dealer_cards)
        print (f"Your cards: [{display_cards_value(player_cards)}], card's value = {player_card_value}")
        #print(show_cards_icons(player_cards, True))
        print (f"Dealer's first hand: [{dealer_cards[0]['card_name']}, ????], card's value = {dealer_cards[0]['card_value']} + ????")
        #print(show_cards_icons(dealer_cards, False))
        # print(f"card's value = {player_card_value}") # debug
        # print(f"card's value = {dealer_cards[0]['card_value']} + ????") # debug
        #player_card_value = int(input(f"enter player_card_value = ")) #debug
        #dealer_card_value = int(input(f"enter dealer_card_value = ")) #debug
        if player_card_value == 21 and dealer_card_value != 21:
            check_winner(player_card_value, dealer_card_value, True)
            print (f"Your cards: [{display_cards_value(player_cards)}]")
            print (f"Dealer's cards: [{display_cards_value(dealer_cards)}]")
            return
        elif dealer_card_value == 21 and player_card_value != 21:
            check_winner(player_card_value, dealer_card_value, True)
            print (f"Your cards: [{display_cards_value(player_cards)}]")
            print (f"Dealer's cards: [{display_cards_value(dealer_cards)}]")
            return
        elif player_card_value < 21:
            while True:
                user_input1 = input("Type 'y' for another card, type 'n' to pass: ").lower()
                if user_input1 == 'n':
                    break
                else:
                    pick_a_card(1, player_cards)
                    player_card_value = calculate_cards_value(player_cards)
                    print (f"Your cards: [{display_cards_value(player_cards)}], card's value = {player_card_value}")
                    #print(f"player_cards_value = {player_card_value}") # debug
                if player_card_value >= 21:
                    break
            os.system('cls')
            print(blackjack_logo)
        if player_card_value == 21:
            print("Lucky!! You got 21, wait for dealer's hand...")
        elif player_card_value > 21:
            print("You got more than 21, wait for dealer's hand...")
        while dealer_card_value <= 16 and player_card_value <= 21 and player_card_value >= dealer_card_value:
                pick_a_card(1, dealer_cards)
                #print (f"Dealer's cards: [{display_cards(dealer_cards)}]")
                dealer_card_value = calculate_cards_value(dealer_cards)

        #print(f"player_cards_value = {player_card_value}") # debug
        #print(show_cards_icons(player_cards, True))
        print (f"Your cards: [{display_cards_value(player_cards)}, card's value = {player_card_value}]")

        #print(f"dealer_cards_value = {dealer_card_value}") # debug
        #print(show_cards_icons(dealer_cards, True))
        print (f"Dealer's cards: [{display_cards_value(dealer_cards)}], card's value = {dealer_card_value}")
        check_winner(player_card_value, dealer_card_value, False)
    
game_is_going = True
while game_is_going:
    game()
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'n':
        game_is_going = False
    else:
        game_is_going = True
        os.system('cls')