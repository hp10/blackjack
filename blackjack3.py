import random
import time
card_values = [['Two', 2], ['Three', 3], ['Four', 4], ['Five', 5], ['Six', 6], ['Seven', 7], ['Eight', 8], ['Nine', 9], ['Ten', 10], ['Jack', 10], ['Queen', 10], ['King', 10], ['Ace', 11]]
card_suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
deck_of_cards = []
for i in range(6): # Generates six decks
    for j in card_suits: # Iterate through card suits
        for k in card_values: # Iterate through card values
            deck_of_cards.append([j, k, False]) # Creates the deck in "['Suit', ['Card Value Text', Int_Value], is_face_down]" format
random.shuffle(deck_of_cards) # Shuffles the deck dumbass

def card_list_to_name(card_list):
    return f'{card_list[1][0]} of {card_list[0]}'
def card_list_to_value(card_list):
    value = 0
    for i in card_list:
        value += i[1][1]
    return value
def draw_card():
    global deck_of_cards
    card = deck_of_cards[0]
    deck_of_cards = deck_of_cards[1:] # Removes first card in the deck, drawing it.
    return card
def hand_list_to_text(hand_list):
    text = ''
    for i in range(len(hand_list)):
        if len(hand_list) - 1 == i:
            text += hand_list[i][1][0] + ' of ' + hand_list[i][0]
        else:
            text += hand_list[i][1][0] + ' of ' + hand_list[i][0] + ', '
    return text

def player_win_lose_push(player_hand, dealer_hand):
    outcome = None
    condition = None
    red = '\u001b[31m'
    green = '\u001b[32m'
    reset = '\u001b[0m'
    player_hand_value = card_list_to_value(player_hand)
    dealer_hand_value = card_list_to_value(dealer_hand)
    if player_hand_value > dealer_hand_value and dealer_hand_value <= 21 and player_hand_value <= 21:
        outcome = f'{green}win{reset}'
        condition = 'Higher value'
    elif dealer_hand_value > player_hand_value and dealer_hand_value <= 21 and player_hand_value <= 21:
        outcome = f'{red}lose{reset}'
        condition = 'Lower value'
    elif player_hand_value > 21 and dealer_hand_value <= 21: # Player busts
        condition = 'Player bust'
        outcome = f'{red}lose{reset}'
    elif dealer_hand_value > 21 and player_hand_value <= 21: # Dealer busts
        condition = 'Dealer bust'
        outcome = f'{green}win{reset}'
    elif player_hand_value == dealer_hand_value: # Push and both under 21
        outcome = f'{green}push{reset}'
        condition = "Push"
    else:
        outcome = 'Unkown'
        outcome = 'Error, no value assigned'
    return (outcome, condition)

def print_hand(player_hand, dealer_hand):
    print(f"""\
----------------
Dealer hand: \u001b[1;4m{card_list_to_value(dealer_hand)}\u001b[0m
{hand_list_to_text(dealer_hand)}
Player hand: \u001b[1;4m{card_list_to_value(player_hand)}\u001b[0m
{hand_list_to_text(player_hand)}""")

def game(betting_enabled = False):
    # Create player and dealer hands
    player_hand = [] # Mimics a standard blackjack deal, as not to interfer with probability for card counting
    dealer_hand = []
    player_hand.append(draw_card())
    face_down_card = draw_card()
    face_down_card[2] = True
    dealer_hand.append(face_down_card)
    player_hand.append(draw_card())
    dealer_hand.append(draw_card())
    # End hand creations
    print_hand(player_hand, dealer_hand)
    print(player_win_lose_push(player_hand, dealer_hand)[0])
    # while True: # Only purpose is to prevent player from entering a character not 'h' or 's'
    #         hit_or_stand = input('Hit or stand (H/S): ').lower()
    #         if hit_or_stand == 'h' or hit_or_stand == 's':
    #             break
    #         else:
    #             print('\x1b[1F\x1b[2K', end='') # Looks crazy but just ANSII code to clear previous line
        
    
game()