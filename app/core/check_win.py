def win(hand):
    if sum(hand) > 21:
        print("dealer vann")
        OrginDictionary["Outcome"][0] -= 1
        OrginDictionary["Money"] -= OrginDictionary["Bet"]
    elif sum(hand) == sum(dealer_card):
        print("Det blev lika!")
        OrginDictionary["Outcome"][1] += 1
    elif sum(dealer_card) > 21:
        print("bot vann")
        OrginDictionary["Outcome"][0] += 1
        OrginDictionary["Money"] += OrginDictionary["Bet"]
        true_count_win()
        true_lst()
    elif sum(hand) > sum(dealer_card):
        print("bot vann")
        OrginDictionary["Outcome"][0] += 1
        OrginDictionary["Money"] += OrginDictionary["Bet"]
        true_count_win()
        true_lst()
    else:
        print("dealer vann")
        OrginDictionary["Money"] -= OrginDictionary["Bet"]
    print("spelarens kort   " + str(hand))
    print("dealers kort  " + str(dealer_card))
    print("bet: " + str(OrginDictionary["Bet"]))
    OrginDictionary["Betted_money"] += OrginDictionary["Bet"]

def split_win(hand):
    if sum(hand) > 21:
        print("dealer vann")
        OrginDictionary["Outcome"][0] -= 1
        OrginDictionary["Money"] -= OrginDictionary["Bet"]
    elif sum(hand) == sum(dealer_card):
        print("Det blev lika!")
        OrginDictionary["Outcome"][1] += 1
    elif sum(dealer_card) > 21:
        print("bot vann")
        OrginDictionary["Outcome"][0] += 1
        OrginDictionary["Money"] += OrginDictionary["Bet"]
        true_count_win()
        true_lst()
    elif sum(hand) > sum(dealer_card):
        print("bot vann")
        OrginDictionary["Outcome"][0] += 1
        OrginDictionary["Money"] += OrginDictionary["Bet"]
        true_count_win()
        true_lst()
    else:
        print("dealer vann")
        OrginDictionary["Outcome"][0] -= 1
        OrginDictionary["Money"] -= OrginDictionary["Bet"]
    OrginDictionary["Betted_money"] += OrginDictionary["Bet"]