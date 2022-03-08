from app.core.main import OrginDictionary

def ace_strategy(hand):
    for i in range(10):
        check_deck()
        if sum(hand) >= 20:
            break
        elif sum(hand) == 19 and dealer_card[1] == 6:
            print("double down4")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 19 and dealer_card[1] != 6:
            break
        elif sum(hand) == 18 and dealer_card[1] in [2, 3, 4, 5, 6]:
            print("double down5")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 18 and dealer_card[1] in [7, 8]:
            break
        elif sum(hand) == 17 and dealer_card[1] in [3, 4, 5, 6]:
            print("double down6")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 16 and dealer_card[1] in [4, 5, 6]:
            print("double down7")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 15 and dealer_card[1] in [4, 5, 6]:
            print("double down")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 14 and dealer_card[1] in [5, 6]:
            print("double down")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 13 and dealer_card[1] in [5, 6]:
            print("double down")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        else:
            hand.append(OrginDictionary["Deck"].pop(0))
    return hand