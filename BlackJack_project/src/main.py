from json.tool import main
import random
from typing import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import seaborn as sns
import numpy as np
import math
import openpyxl
import scipy
from scipy.stats import norm
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from tkinter import *
from tkinter.ttk import Combobox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from sqlalchemy import column


true_count_win_lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lst = []


def true_lst():
    lst.append(OrginDictionary["True_count"])
    return lst


# kosntig måsta fixas
def true_count_win():
    if OrginDictionary["True_count"] <= 6 and OrginDictionary["True_count"] >= -6:
        true_count_win_lst[OrginDictionary["True_count"] + 6] += 1


def running_count_func(hand):
    minus = [11, 10, 1]
    zero = [9, 8, 7]
    plus = [6, 5, 4, 3, 2]
    for i in range(0, len(hand)):
        if hand[i] in minus:
            OrginDictionary["Running_count"] -= 1
        if hand[i] in plus:
            OrginDictionary["Running_count"] += 1
    return OrginDictionary["Running_count"]


def bet_amount(bet1):
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


def check_ace(hand):
    for n, card in enumerate(hand):
        if card == 11:
            return True
        else:
            return False
            # hand[n] = 1


running_count_change = []
true_count_change = []
money_change = []
money_change2 = []
money_change3 = []

OrginDictionary = {
    "Money": 10000,
    "Bet": 10,
    "Bet_split": [0, 0],
    "Outcome": [0, 0, 0],
    "Cards_played": 0,
    "True_count": 0,
    "Running_count": 0,
    "Betted_money": 0,
    "Deck": [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11],
}
ChangeDictionary = {
    "Running_count": [],
    "True_count": [], }


def main_loop(iterations, deck_amount):

    global OrginDictionary
    global running_count_change
    global true_count_change
    OrginDictionary["Deck"] = [2, 3, 4, 5, 6, 7,
                               8, 9, 10, 10, 10, 10, 11] * 4 * deck_amount
    random.shuffle(OrginDictionary["Deck"])

    def check_splitdb(hand):
        if player_card_split1 == hand:
            OrginDictionary["Bet_split"][0] *= 2
        elif player_card_split2 == hand:
            OrginDictionary["Bet_split"][1] *= 2

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
                print("double down")
                hand.append(OrginDictionary["Deck"].pop(0))
                OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
                check_splitdb(hand)
                break
            elif sum(hand) == 10 and 3 <= dealer_card[1] <= 9:
                print("double down")
                hand.append(OrginDictionary["Deck"].pop(0))
                OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
                check_splitdb(hand)
                break
            elif sum(hand) == 9 and 6 >= dealer_card[1] >= 3:
                print("double down")
                hand.append(OrginDictionary["Deck"].pop(0))
                OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
                check_splitdb(hand)
                break
            else:
                hand.append(OrginDictionary["Deck"].pop(0))
        return hand

    def ace_strategy(hand):
        for i in range(10):
            check_deck()
            if sum(hand) >= 20:
                break
            elif sum(hand) == 19 and dealer_card[1] == 6:
                print("double down")
                hand.append(OrginDictionary["Deck"].pop(0))
                OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
                check_splitdb(hand)
                break
            elif sum(hand) == 19 and dealer_card[1] != 6:
                break
            elif sum(hand) == 18 and dealer_card[1] in [2, 3, 4, 5, 6]:
                print("double down")
                hand.append(OrginDictionary["Deck"].pop(0))
                OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
                check_splitdb(hand)
                break
            elif sum(hand) == 18 and dealer_card[1] in [7, 8]:
                break
            elif sum(hand) == 17 and dealer_card[1] in [3, 4, 5, 6]:
                print("double down")
                hand.append(OrginDictionary["Deck"].pop(0))
                OrginDictionary["Bet"] = OrginDictionary["Bet"] * 2
                check_splitdb(hand)
                break
            elif sum(hand) == 16 and dealer_card[1] in [4, 5, 6]:
                print("double down")
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

    def check_deck():
        if len(OrginDictionary["Deck"]) == 0:
            OrginDictionary["Deck"] = [2, 3, 4, 5, 6, 7,
                                       8, 9, 10, 10, 10, 10, 11] * 4 * deck_amount
            random.shuffle(OrginDictionary["Deck"])
            OrginDictionary["cards_played"] = 0
            OrginDictionary["true_count"] = 0
            OrginDictionary["running_count"] = 0

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

    def splitting(split1, split2):
        if len(split1) == 0 and len(split2) == 0:
            check_deck()
            split1.append(player_card[0])
            split2.append(player_card[1])

        while len(split1) != 2 and len(split2) != 2:
            check_deck()
            split1.append(OrginDictionary["Deck"].pop(0))
            split1.append(OrginDictionary["Deck"].pop(0))

        return split1, split2

    def ifsplit():
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

    for i in range(iterations):
        check_deck()
        print(
            "\n"
            + "cards played "
            + str(OrginDictionary["Cards_played"])
            + "\n"
            + "running count: "
            + str(OrginDictionary["Running_count"])
            + "\n"
            + "true count: "
            + str(OrginDictionary["True_count"])
            + "\n"
            + str(OrginDictionary["Money"])
        )

        # choose between bet_amount, bet_amount2 and kelly_criterion

        bet_strategy = 10
        OrginDictionary["bet"] = bet_strategy
        bet_split1 = OrginDictionary["bet"]
        bet_split2 = OrginDictionary["bet"]
        player_card = []
        dealer_card = []
        player_card_split1 = []
        player_card_split2 = []

        while sum(dealer_card) < 17:
            check_deck()
            dealer_card.append(OrginDictionary["Deck"].pop(0))

        while len(player_card) != 2:
            check_deck()
            player_card.append(OrginDictionary["Deck"].pop(0))
        print(" ")
        if player_card[0] == player_card[1]:
            ifsplit()
        elif player_card[0] == 11 or player_card[1] == 11:
            ace_strategy(player_card)
        else:
            basic_strategy(player_card)

        if sum(player_card_split1) > 21:
            check_ace(player_card_split1)
            basic_strategy(player_card_split1)
        if sum(player_card_split2) > 21:
            check_ace(player_card_split2)
            basic_strategy(player_card_split2)
        if sum(player_card) > 21:
            check_ace(player_card)
            basic_strategy(player_card)
        if sum(dealer_card) > 21:
            check_ace(dealer_card)
            while sum(dealer_card) < 17:
                check_deck()
                dealer_card.append(OrginDictionary["Deck"].pop(0))

        # calcuatle cards played
        OrginDictionary["Cards_played"] += (
            len(player_card)
            + len(dealer_card)
            + len(player_card_split1)
            + len(player_card_split2)
        )
        # calculate true count

        running_count_func(player_card)
        running_count_func(dealer_card)
        running_count_func(player_card_split1)
        running_count_func(player_card_split2)
        try:
            OrginDictionary["True_count"] = round(
                OrginDictionary["Running_count"] /
                round(((52 * deck_amount) -
                        OrginDictionary["Cards_played"]) / 52)
            )
        except ZeroDivisionError:
            OrginDictionary["True_count"] = OrginDictionary["Running_count"]

        if sum(player_card) == 21 and len(player_card) == 2:
            OrginDictionary["Bet"] *= 1.5
        if sum(player_card_split1) == 21 and len(player_card_split1) == 2:
            bet_split1 = bet_split1 * 1.5
        if sum(player_card_split2) == 21 and len(player_card_split2) == 2:
            bet_split2 = bet_split2 * 1.5

        round(OrginDictionary["Bet"])
        if len(player_card_split1) != 0:
            split_win(player_card_split1, bet_split1)
            split_win(player_card_split2, bet_split2)
            print(bet_split1)
            print(bet_split2)

            print(str(player_card_split2) + str(player_card_split1))
            print("dealers kort" + str(dealer_card))

            print(" ")
            print(player_card_split2)
            print(player_card_split1)
        else:
            win(player_card)
        running_count_change.append(OrginDictionary["Running_count"])
        true_count_change.append(OrginDictionary["True_count"])

    print("antalet gågner botten van    " + str(OrginDictionary["Outcome"][0]))
    print("antalet gånger det blev lika     " +
            str(OrginDictionary["Outcome"][1]))
    print("pengar: " + str(OrginDictionary["Money"]))
    print("pengar bettad:" + str(OrginDictionary["Betted_money"]))


X_axis = range(len(running_count_change))
df_count = pd.DataFrame(
    {
        "running_count": running_count_change,
        "true_count": true_count_change,
        "xaxis": X_axis,
    }
)

#house_edge = round(
 #   ((10000 - OrginDictionary["Money"]) / OrginDictionary["Betted_money"]) * 100, 2)
#print(str(house_edge) + "%")
house_edge = 0
xaxis = range(len(money_change))


true_prob = true_count_win_lst
x_list = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
df_money = {"money_change": money_change, "xaxis": xaxis}



#################################GUI########################







# df_money2 = pd.DataFrame({'xaxis':xaxis,  'money_change': money_change,  'money_change2':money_change2, 'money_change3':money_change3})
# df_money2 = df_money2.melt('xaxis', var_name='cols',  value_name='vals')
# g = sns.lineplot(x="xaxis", y="vals", hue='cols', data=df_money2)
# plt.xlabel('Antal gånger spelat')
# plt.ylabel('Pengar')
# plt.title('Pengar')
# plt.show()


"""
fig, ax = plt.subplots()
sns.lineplot(data=df_money, x="xaxis", y="money_change", ax=ax)
chart_type = FigureCanvasTkAgg(fig, root)
chart_type.get_tk_widget().pack()
plt.xlabel("Games played")
plt.ylabel("Money")
plt.title("Betting with units in regard to current bankroll")
ax2 = plt.axes([0.25, 0.55, 0.2, 0.2], facecolor="lightgrey")
sns.lineplot(data=df_money, x="xaxis", y="money_change", ax=ax2)
ax2.set_title("zoom")
ax2.set_xlim([0, 5000])
ax2.set_ylim([9500, 11000])


sns.distplot(lst, fit=norm)
plt.xlabel("True count")
plt.ylabel("Distrubution")
plt.title("Distrubution of winning")
plt.show()

df_trueprob = pd.DataFrame({"true_prob": true_prob, "xaxis": x_list})
sns.barplot(data=df_trueprob, x="xaxis", y="true_prob")
plt.xlabel("True count")
plt.ylabel("Games won")
plt.title("True count distrubution")
plt.show()

figure = plt.Figure(figsize=(6,5), dpi=100)
ax = figure.add_subplot(111)
chart_type = FigureCanvasTkAgg(figure, root)
chart_type.get_tk_widget().pack()
sns.lineplot(data=df_count.head(2000), x="xaxis", y="running_count")
plt.ylabel("Running count")
plt.xlabel("Games played")






fig2, ax = plt.subplots()
sns.lineplot(
    data=df_count.head(1000),
    x="xaxis",
    y="true_count",
    linewidth=2,
    alpha=0.3,
    linestyle="--",
    ax=ax,
)
sns.regplot(data=df_count.head(1000), x="xaxis", y="true_count", scatter=False)
plt.ylabel("True count")
plt.xlabel("games")
plt.title("True count change")
plt.show()

fig3, ax = plt.subplots()
df_count = df_count.melt("xaxis", var_name="cols", value_name="vals")
f = sns.violinplot(y="vals", hue="cols", data=df_count)
plt.show()


# df_trueprob.to_excel('Gymnasiearbete_excel.xlsx', index=False)


"""
