import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
import openpyxl 
import scipy
from scipy.stats import norm
sns.set_palette("Blues_d")


# 2, 3, 4, 5, 6, 7, 8, 9, 10, J,  Q,  K,  A

minus_one = 0
minus_two = 0
minus_three = 0
minus_four = 0
minus_five = 0
minus_six = 0
minus_seven = 0
zero = 0
plus_one = 0
plus_two = 0
plus_three = 0
plus_four = 0
plus_five = 0
plus_six = 0
plus_seven = 0

lst = []

def true_lst():    
    if true_count == -6:
        lst.append(-6)
    elif true_count == -5:
        lst.append(-5)
    elif true_count == -4:
        lst.append(-4)
    elif true_count == -3:
        lst.append(-3)
    elif true_count == -2:
        lst.append(-2)
    elif true_count == -1:
        lst.append(-1)
    elif true_count == 0:
        lst.append(0)
    elif true_count == 1:
        lst.append(1)
    elif true_count == 2:
        lst.append(2)
    elif true_count == 3:
        lst.append(3)
    elif true_count == 4:
        lst.append(4)
    elif true_count == 5:
        lst.append(5)
    elif true_count == 6:
        lst.append(6)
    return lst
    

def true_count_win():
    global true_count
    global minus_one
    global minus_two 
    global minus_three 
    global minus_four 
    global minus_five
    global minus_six  
    global minus_seven
    global zero 
    global plus_one 
    global plus_two 
    global plus_three 
    global plus_four 
    global plus_five 
    global plus_six 
    global plus_seven
    if true_count == 7:
        minus_seven += 1
    elif true_count == -6:
        minus_six += 1
    elif true_count == -5:
        minus_five += 1
    elif true_count == -4:
        minus_four += 1
    elif true_count == -3:
        minus_three += 1
    elif true_count == -2:
        minus_two += 1
    elif true_count == -1:
        minus_one += 1
    elif true_count == 0:
        zero += 1
    elif true_count == 1:
        plus_one += 1
    elif true_count == 2:
        plus_two += 1
    elif true_count == 3:
        plus_three += 1
    elif true_count == 4:
        plus_four += 1
    elif true_count == 5:
        plus_five += 1
    elif true_count == 6:
        plus_six += 1
    elif true_count == 7:
        plus_seven += 1
deck_shuffle = 0

def check_deck():
    global deck_shuffle
    global deck_amount
    global deck
    global cards_played
    global true_count
    global running_count
    if len(deck) == 0:
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * deck_amount
        random.shuffle(deck)
        deck_shuffle += 1
        cards_played = 0
        true_count = 0
        running_count = 0

def running_count_func(hand):
    global running_count
    global true_count
    global deck_amount
    minus = [11, 10, 1]
    zero = [9, 8, 7]
    plus = [6, 5, 4, 3, 2]
    for i in range(0, len(hand)):
        if hand[i] in minus:
            running_count -= 1
        if hand[i] in plus:
            running_count += 1
    return running_count

def bet_amount(bet1):
    global true_count
    if true_count <1:
        bet1 = 5
    elif 6 >= true_count >= 1:
        bet1 = (money * 0.001)*(true_count + 1) 
    else:
        bet1 = (money * 0.001) * 7
    if bet1 < 5:
        bet1 = 5

    return round(bet1)

def bet_amount2(bet1):
    global true_count
    if true_count < 0:
        bet1 = 5
    elif 6 >= true_count >= 1:
        bet1 = 10 * (true_count + 1)
    else:
        bet1 = 10 * 7
    return bet1

def Kelly_criterion(bet1):
    global true_count
    global money
    if true_count <2:
        bet1 = 5
    elif 6 >= true_count >= 2:
        bet1 = (money * 0.001) * (true_count - 1)
    else:
        bet1 = (money * 0.001) * 5

    if bet1 < 5:
        bet1 = 5
    
    return round(abs(bet1))

def thorp(bet1):
    global true_count
    global money
    HLI = true_count/(52)
    if HLI <= 2:
        bet1 = money * 0.001
    elif 2 < HLI <= 10:
        bet1 = money * 0.001 * HLI/2
    elif HLI >= 10:
        bet1 = money * 0.001 * 5
    
    return round(abs(bet1))


def check_splitdb(hand):
    global bet_split1
    global bet_split2
    if player_card_split1 == hand:
        bet_split1 = bet_split1 * 2
    elif player_card_split2 == hand:
        bet_split2 = bet_split2 * 2

def basic_strategy(hand, dealer):
    global bet
    for _ in range(10):
        check_deck()
        if sum(hand) > 21:
            check_ace(hand)
        elif sum(hand) >= 17:
            break
        elif sum(hand) in [16,15,14,13] and dealer[1] <= 6:
            break
        elif sum(hand) == 12 and 4 <= dealer[1] <= 6:
            break
        elif sum(hand) == 11:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet*2
            check_splitdb(hand)
            break
        elif sum(hand) == 10 and 3 <= dealer[1] <= 9:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet*2
            check_splitdb(hand)
            break
        elif sum(hand) == 9 and 6 >= dealer[1] >= 3:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet*2
            check_splitdb(hand)
            break
        else:
            hand.append(deck.pop(0))



def ace_strategy(hand, dealer):
    global bet
    for i in range(10):
        check_deck()
        if sum(hand) >= 20:
            break
        elif sum(hand) == 19 and dealer[1] == 6:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 19 and dealer[1] != 6:
            break
        elif sum(hand) == 18 and dealer[1] in [2,3,4,5,6]:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 18 and dealer[1] in [7,8]:
            break
        elif sum(hand) == 17 and dealer[1] in [3,4,5,6]:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet * 2
            check_splitdb(hand)
            break
        elif sum(hand) == 16 and dealer[1] in [4,5,6]:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet*2
            check_splitdb(hand)
            break
        elif sum(hand) == 15 and dealer[1] in [4,5,6]:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet*2
            check_splitdb(hand)
            break
        elif sum(hand) == 14 and dealer[1] in [5,6]:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet*2
            check_splitdb(hand)
            break
        elif sum(hand) == 13 and dealer[1] in [5,6]:
            print('double down')
            hand.append(deck.pop(0))
            bet = bet*2
            check_splitdb(hand)
            break
        else:
            hand.append(deck.pop(0))

def check_ace(hand):
    for n, card in enumerate(hand):
        if card == 11:
            hand[n] = 1

def splitting(hand, hand2):
    if len(hand) == 0 and len(hand2) == 0:
        check_deck()
        hand.append(player_card[0])
        hand2.append(player_card[1])

    while len(hand) != 2 and len(hand2) != 2:
        check_deck()
        hand.append(deck.pop(0))
        hand2.append(deck.pop(0))
    
bet = 0
bet_split1 = 0
bet_split2 = 0
money_betted = 0
win_count = 0
equal_count = 0
cards_played = 0
true_count = 0
running_count = 0

money = 10000
deck_amount = 4


running_count_change = []
true_count_change = []

money_change = []
money_change2 = []
money_change3 = []
money_change4 = []
money_change5 = []
money_change6 = []
money_change7 = []
money_change8 = []
money_change9 = []
money_change10 = []
def money_changefunc():
    global n
    global money
    global money_change
    global money_change2 
    global money_change3
    global money_change4
    global money_change5
    if n == 0:
        money_change.append(money)
    elif n == 1:
        money_change2.append(money)
    elif n == 2:
        money_change3.append(money)
    elif n == 3:
        money_change4.append(money)
    elif n == 4:
        money_change5.append(money)

def main_loop(iteration):
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * deck_amount
        random.shuffle(deck)
        money = int(input('How much money do you want to bet?'))
        bet = 0
        bet_split1 = 0
        bet_split2 = 0
        money_betted = 0
        win_count = 0
        equal_count = 0
        cards_played = 0
        true_count = 0
        running_count = 0
        times = input('How many times do you want to play?')
        for i in range(iteration):
            check_deck()
            print()
            print('cards played ' + str(cards_played))
            print('running count: ' + str(running_count))
            print('true count: ' + str(true_count))
            print(money)

            # choose between bet_amount, bet_amount2 and kelly_criterion
            bacis_strategy1 = 10
            bet_strategy = 10
            bet = bet_strategy
            bet_split1 = bet_strategy
            bet_split2 = bet_strategy
            player_card = []
            dealer_card = []
            player_card_split1 = []
            player_card_split2 = []

            while sum(dealer_card) < 17:
                check_deck()
                dealer_card.append(deck.pop(0))

            while len(player_card) != 2:
                check_deck()
                player_card.append(deck.pop(0))
            print(' ')
            if player_card[0] == player_card[1]:
                for i in range(10):
                    check_deck()
                    if player_card[0] == 10:
                        break
                    elif player_card[1] == 9 and dealer_card[1] in [7,  10, 11]:
                        basic_strategy(player_card)
                        break
                    elif player_card[0] == 7 and dealer_card[1] > 7:
                        basic_strategy(player_card)
                        break
                    elif player_card[0] == 6 and dealer_card[1] in [7, 8, 9, 10, 11]:
                        basic_strategy(player_card)
                        break
                    elif player_card[0] == 4 and dealer_card[1] in [3,4,5,8,9,10,11]:
                        basic_strategy(player_card)
                        break
                    elif player_card[0] == 3 and dealer_card[1] > 7:
                        basic_strategy(player_card)
                        break
                    elif player_card[0] == 2 and dealer_card[1] > 7:
                        basic_strategy(player_card)
                        break
                    else:
                        basic_strategy(player_card)
                        if len(player_card_split1) == 0 and len(player_card_split2) == 0:
                            player_card_split1.append(player_card[0])
                            player_card_split2.append(player_card[0])
                            check_deck()
                            player_card_split1.append(deck.pop(0))
                            check_deck()
                            player_card_split2.append(deck.pop(0))
                        if player_card_split1[0] == 11 or player_card_split1[1] == 11:
                            ace_strategy(player_card_split1)
                        elif player_card_split2[0] == 11 or player_card_split2[1] == 11:
                            ace_strategy(player_card_split2)
                        else:
                            basic_strategy(player_card_split1)
                            basic_strategy(player_card_split2)
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
                    dealer_card.append(deck.pop(0))

        def win(hand, bet):
            global money
            global equal_count
            global win_count
            global money_betted
            if sum(hand) > 21:
                print('dealer vann')
                money -= bet
            elif sum(hand) == sum(dealer_card):
                print('Det blev lika!')
                equal_count += 1
            elif sum(dealer_card) > 21:
                print('bot vann')
                win_count += 1
                money += bet
                true_count_win()
                true_lst()
            elif sum(hand) > sum(dealer_card):
                print('bot vann')
                win_count += 1
                money += bet
                true_count_win()
                true_lst()
            else:
                print('dealer vann')
                money -= bet
            print('spelarens kort   ' + str(hand))
            print('dealers kort  ' + str(dealer_card))
            print('bet: ' + str(bet))
            money_betted += bet

        def split_win(hand, bet):
            global money
            global equal_count
            global win_count
            global money_betted
            if sum(hand) > 21:
                print('dealer vann')
                win_count -= 1
                money -= bet
            elif sum(hand) == sum(dealer_card):
                print('Det blev lika!')
                equal_count += 1
            elif sum(dealer_card) > 21:
                print('bot vann')
                win_count += 1
                money += bet
                true_count_win()
                true_lst()
            elif sum(hand) > sum(dealer_card):
                print('bot vann')
                win_count += 1
                money += bet
                true_count_win()
                true_lst()
            else:
                print('dealer vann')
                win_count -= 1
                money -= bet
            money_betted += bet

        # calcuatle cards played
        cards_played += len(player_card) 
        cards_played += len(dealer_card)  
        cards_played += len(player_card_split1)  
        cards_played += len(player_card_split2)
        # calculate true count
        
        running_count_func(player_card)
        running_count_func(dealer_card)
        running_count_func(player_card_split1)
        running_count_func(player_card_split2)
        try:
            true_count = round(running_count/round(((52*deck_amount)-cards_played)/52))
        except ZeroDivisionError:
            true_count = running_count
        
        if sum(player_card) == 21 and len(player_card) == 2:
            bet = bet * 1.5
        if sum(player_card_split1) == 21 and len(player_card_split1) == 2:
            bet_split1 = bet_split1 * 1.5
        if sum(player_card_split2) == 21 and len(player_card_split2) == 2:
            bet_split2 = bet_split2 * 1.5

        round(bet)
        if len(player_card_split1) != 0:
            split_win(player_card_split1, bet_split1)
            split_win(player_card_split2, bet_split2)
            print(bet_split1)
            print(bet_split2)

            print(str(player_card_split2) + str(player_card_split1))
            print('dealers kort' + str(dealer_card))

            print(' ')
            print(player_card_split2)
            print(player_card_split1)
        else:
            win(player_card, bet)
        money_changefunc()
        running_count_change.append(running_count)
        true_count_change.append(true_count)
        


print('antalet gågner botten van    ' + str(win_count))
print('antalet gånger det blev lika     ' + str(equal_count))
print('pengar: ' + str(money))
print('pengar bettad:' + str(money_betted))


house_edge = round(((10000 - money)/money_betted) * 100, 2)
print(str(house_edge) + '%')
xaxis = range(len(money_change)) 

true_prob = [minus_six, minus_five, minus_four, minus_three, minus_two, minus_one, zero, plus_one, plus_two, plus_three, plus_four, plus_five, plus_six]
x_list = [-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6]
df_money = {'money_change': money_change, 'xaxis':xaxis}


#df_money2 = pd.DataFrame({'xaxis':xaxis,  'money_change': money_change,  'money_change2':money_change2, 'money_change3':money_change3})
#df_money2 = df_money2.melt('xaxis', var_name='cols',  value_name='vals')
#g = sns.lineplot(x="xaxis", y="vals", hue='cols', data=df_money2)
#plt.xlabel('Antal gånger spelat')
#plt.ylabel('Pengar')
#plt.title('Pengar')
#plt.show()



fig, ax = plt.subplots()
sns.lineplot(data=df_money,
x='xaxis',
y='money_change',
ax=ax)
plt.xlabel('Games played')
plt.ylabel('Money')
plt.title(str(bet_strategy))
ax2 = plt.axes([0.25, 0.55, .2, .2], facecolor='lightgrey')
sns.lineplot(data=df_money,
x='xaxis',
y='money_change',
ax=ax2)
ax2.set_title('zoom')
ax2.set_xlim([0,5000])
ax2.set_ylim([9500,11000])
plt.show()

sns.distplot(lst, fit=norm)
plt.legend()
plt.xlabel('True count')
plt.ylabel('Distrubution')
plt.title('Distrubution of winning')
plt.show()

df_trueprob = pd.DataFrame({'true_prob': true_prob, 'xaxis':x_list})
sns.barplot(data=df_trueprob,
x='xaxis',
y='true_prob')
plt.xlabel('True count')
plt.ylabel('Games won')
plt.title('True count distrubution')
plt.show()

X_axis = range(len(running_count_change))
df_count = pd.DataFrame({'running_count': running_count_change, 'true_count':true_count_change, 'xaxis':X_axis})

sns.lineplot(data=df_count.head(2000),
x='xaxis'
,y='running_count')
plt.ylabel('Running count')
plt.xlabel('Games played')
plt.show()

fig2, ax = plt.subplots()
sns.lineplot(data=df_count.head(1000),
x='xaxis'
,y='true_count',
linewidth=2,
alpha=0.3,
linestyle='--',
ax=ax)
sns.regplot(data=df_count.head(1000),
x='xaxis',
y='true_count',
scatter=False)
plt.ylabel('True count')
plt.xlabel('games')
plt.title('True count change')
plt.show()

fig3, ax=plt.subplots()
df_count = df_count.melt('xaxis', var_name='cols',  value_name='vals')
f = sns.violinplot(y="vals", hue='cols', data=df_count)
plt.show()



