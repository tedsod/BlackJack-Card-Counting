

def bet_amount(bet1, OrginDictionary):
    if OrginDictionary["True_count"] < 1:
        bet1 = 5
    elif 6 >= OrginDictionary["True_count"] >= 1:
        bet1 = (OrginDictionary["Money"] * 0.001) * \
            (OrginDictionary["True_count"] + 1)
    else:
        bet1 = (OrginDictionary["Money"] * 0.001) * 7
    if bet1 < 5:
        bet1 = 5

    return round(bet1)


def bet_amount2(bet1, tc):
    if tc < 0:
        bet1 = 5
    elif 6 >= tc >= 1:
        bet1 = 10 * (tc + 1)
    else:
        bet1 = 10 * 7
    return bet1


def Kelly_criterion(bet1, money, tc):
    if tc < 2:
        bet1 = 5
    elif 6 >= tc >= 2:
        bet1 = (money * 0.001) * (tc - 1)
    else:
        bet1 = (money * 0.001) * 5

    if bet1 < 5:
        bet1 = 5

    return round(abs(bet1))


def thorp(bet1, money, tc):
    HLI = tc / (52)
    if HLI <= 2:
        bet1 = money * 0.001
    elif 2 < HLI <= 10:
        bet1 = money * 0.001 * HLI / 2
    elif HLI >= 10:
        bet1 = money * 0.001 * 5

    return round(abs(bet1))