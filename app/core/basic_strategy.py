
def basic_strategy(hand):
    for _ in range(10):
        check_deck()
        if sum(hand) > 21:
            check_ace(hand)
        elif sum(hand) >= 17:
            break
        elif sum(hand) in [16, 15, 14, 13] and dealer_card[1] <= 6:
            break
        elif sum(hand) == 12 and 4 <= dealer_card[1] <= 6:
            break
        elif sum(hand) == 11:
            print("double down1")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 10 and 3 <= dealer_card[1] <= 9:
            print("double down2")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 9 and 6 >= dealer_card[1] >= 3:
            print("double down3")
            hand.append(OrginDictionary["Deck"].pop(0))
            OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
            check_splitdb(hand)
            break
        else:
            hand.append(OrginDictionary["Deck"].pop(0))
    return hand