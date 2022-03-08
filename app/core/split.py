from app.core.main import OrginDictionary, player_card


def splitting(split1, split2):
    if len(split1) == 0 and len(split2) == 0:
        check_deck()
        split1.append(player_card[0])
        split2.append(player_card[1])

    while len(split1) <= 2 and len(split2) <= 2:
        check_deck()
        split1.append(OrginDictionary["Deck"].pop(0))
        check_deck()
        split2.append(OrginDictionary["Deck"].pop(0))

    return split1, split2

def ifsplit(player_card_split1, player_card_split2):
    for i in range(10):
        check_deck()
        if player_card[0] == 10:
            break
        elif player_card[1] == 9 and dealer_card[1] in [7, 10, 11]:
            basic_strategy(player_card)
            break
        elif player_card[0] == 7 and dealer_card[1] > 7:
            basic_strategy(player_card)
            break
        elif player_card[0] == 6 and dealer_card[1] in [7, 8, 9, 10, 11]:
            basic_strategy(player_card)
            break
        elif player_card[0] == 4 and dealer_card[1] in [3, 4, 5, 8, 9, 10, 11]:
            basic_strategy(player_card)
            break
        elif player_card[0] == 3 and dealer_card[1] > 7:
            basic_strategy(player_card)
            break
        elif player_card[0] == 2 and dealer_card[1] > 7:
            basic_strategy(player_card)
            break
        else:
            player_card_split1, player_card_split2 = splitting(
                player_card_split1, player_card_split2
            )
            if player_card_split1[0] == 11 or player_card_split1[1] == 11:
                ace_strategy(player_card_split1)
            elif player_card_split2[0] == 11 or player_card_split2[1] == 11:
                ace_strategy(player_card_split2)
            else:
                basic_strategy(player_card_split1)
                basic_strategy(player_card_split2)

def check_splitdb(hand):
    if player_card_split1 == hand:
        OrginDictionary["Bet_split"][0] *= 2
    elif player_card_split2 == hand:
        OrginDictionary["Bet_split"][1] *= 2