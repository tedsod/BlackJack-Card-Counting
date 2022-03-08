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






    def check_deck():
        if len(OrginDictionary["Deck"]) == 0:
            OrginDictionary["Deck"] = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * deck_amount
            random.shuffle(OrginDictionary["Deck"])
            OrginDictionary["cards_played"] = 0
            OrginDictionary["true_count"] = 0
            OrginDictionary["running_count"] = 0



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
        print(pd.DataFrame(OrginDictionary))

        # choose between bet_amount, bet_amount2 and kelly_criterion

        bet_strategy = 10
        print(OrginDictionary["bet"])
        OrginDictionary["bet"] = 10
        print(OrginDictionary["bet"])
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
            ifsplit(player_card_split1, player_card_split2)
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
            split_win(player_card_split1)
            split_win(player_card_split2)
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


main_loop(10, 2)


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
