    
carts = {
   '2♠️': 2, '3♠️': 3, '4♠️': 4, '5♠️': 5, '6♠️': 6, '7♠️': 7, '8♠️': 8, '9♠️': 9, '10♠️': 10, 'J♠️': 10, 'Q♠️': 10, 'K♠️': 10, 'A♠️': 11,
   
   '2♥️': 2, '3♥️': 3, '4♥️': 4, '5♥️': 5, '6♥️': 6, '7♥️': 7, '8♥️': 8, '9♥️': 9, '10♥️': 10, 'J♥️': 10, 'Q♥️': 10, 'K♥️': 10, 'A♥️': 11,
   
    '2♦️': 2, '3♦️': 3, '4♦️': 4, '5♦️': 5, '6♦️': 6, '7♦️': 7, '8♦️': 8, '9♦️': 9, '10♦️': 10, 'J♦️': 10, 'Q♦️': 10, 'K♦️': 10, 'A♦️': 11,
   '2♣️': 2, '3♣️': 3, '4♣️': 4, '5♣️': 5, '6♣️': 6, '7♣️': 7, '8♣️': 8, '9♣️': 9, '10♣️': 10, 'J♣️': 10, 'Q♣️': 10, 'K♣️': 10, 'A♣️': 11}


import random

ordered_keys = list(carts.keys())
random.shuffle(ordered_keys)
shuffled_deck = {key: carts[key] for key in ordered_keys}
# shuffled_deck = dict(random.sample(carts.items(), len(carts)))
shuffled_list = [[key, value] for key, value in shuffled_deck.items()]

print(shuffled_deck)
print(shuffled_list)

active=True
moves=0
player_hand=shuffled_list[:3:2]
diller_hand=shuffled_list[1:4:2]
new_list=shuffled_list[4:]
print(f"Deck without first four cards: {new_list}")
print(f"Player's hand: {player_hand}")
print(f"Diller's hand: {diller_hand}")

diller_points=diller_hand[0][1]+diller_hand[1][1]
player_points=player_hand[0][1]+player_hand[1][1]

print(f"Player's points: {player_points}")
print(f"Diller's points: {diller_points}")


while active:

    if player_points==21 and diller_points==21:
        print('You have the same quantity of points. Tie!')
        break
    if player_points==21 and diller_points<player_points:
        print(f'Dealer has {diller_points} points and you have {player_points}. Player won.')
    elif player_points>21:
        print('You have more than 21 points. You lost.')
        break
    elif player_points < 21:

        print('Do you want to take an additional card? Input "yes" or "no"')
        hit = input('Your answer: ').lower().strip()

        while hit == 'yes':
            next_card = new_list[0+moves]
            moves += 1
            player_hand.append([next_card])
            player_points += next_card[1]
            print(f'Your hand: {player_hand}')
            print(f'Your points: {player_points}')

            if player_points > 21:
                print('You have more than 21 points. You lost.')
                active = False
                break

            # if player_points==21:
            #     print("You have 21 points. You won ")
            #     break
            # what if diller has the same points? therefore, player should wait untill diller will start
            # his cycle, but 'continue' doesn't work in this case and it is impossible to use 'break'
            # ? it's possible not to use this condition but it will be strange if the player has 21 points
            # and the program is asking him whether he wants to take an additional card

            print('Do you want to take another card? Input "yes" or "no"')
            hit = input('Your answer: ').lower().strip()


        if hit == 'no':

            while diller_points < 17 or player_points<diller_points<17:
                dillers_next_card = new_list[moves]
                diller_hand.append([dillers_next_card])
                diller_points += dillers_next_card[1]
                moves += 1
                print(f"Dealer's hand: {diller_hand}")
                print(f"Dealer's points: {diller_points}")

                if diller_points > 21:
                    print('Dealer has more than 21 points. Player won.')
                    break
                if diller_points>player_points:
                    print('Diller won')
                    break
                if diller_points>17 and diller_points<player_points:
                    print(f'Dealer has {diller_points} points and you have {player_points}. Player won.')
                elif diller_points==player_points:
                    print('You have the same quantity of points. Tie!')
                    break

            if diller_points>21:
                print('Dealer has more than 21 points. Player won.')
                break

            if 17<diller_points<=21 and diller_points>player_points:
                print(f'Dealer has {diller_points} points and you have {player_points}. Diller won.')
                break

            elif 17<diller_points<21 and diller_points<player_points:
                print(f'Dealer has {diller_points} points and you have {player_points}. Player won.')
                break

            elif diller_points==player_points:
                print('You have the same quantity of points. Tie!')
                break
        

                

