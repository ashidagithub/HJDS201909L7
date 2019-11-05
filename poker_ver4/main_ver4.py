# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
# 完成一个荷官洗牌发牌给n个玩家的模拟程序
# ------------------------(max to 80 columns)-----------------------------------

#from my_mods import *
from Machine.standard_machine import *
from Dealer.Mike import *

# Phase 1 -------------------------------------------------------
# 从机器取一副新牌并写入一个文件
deck = []
create_deck(deck)
fname = 'NewDeck_54.txt'
record_deck(deck, fname)

# Phase 2 -------------------------------------------------------
# 重新从机器拿一副牌，并重新洗牌并将结果写入另一个文件
deck = []
create_deck(deck)
shuffle_deck(deck)
fname = 'NewDeck_54_Shuffled.txt'
record_deck(deck, fname)

# Phase 3 -------------------------------------------------------
# 给某个玩家发几张牌
card_num = 5
p1_deck = []
deal_to_a_player(deck, card_num, p1_deck)
fname = 'Player1Cards.txt'
record_deck(p1_deck, fname)
fname = 'RemainedDeck.txt'
record_deck(deck, fname)

# Phase 3 -------------------------------------------------------
# 给多个玩家发牌
# method 1:
# 重新从机器拿一副牌，并重新洗牌
deck = []
create_deck(deck)
shuffle_deck(deck)

numOfPlayers = 3    #
cardsOfPlayer = int(len(deck) / numOfPlayers)

p1_deck = []
deal_to_a_player(deck, cardsOfPlayer, p1_deck)
record_deck(p1_deck, 'p1_deck.txt')

p2_deck = []
deal_to_a_player(deck, cardsOfPlayer, p2_deck)
record_deck(p2_deck, 'p2_deck.txt')

p3_deck = []
deal_to_a_player(deck, cardsOfPlayer, p3_deck)
record_deck(p3_deck, 'p3_deck.txt')

# Phase 4 -------------------------------------------------------
# 给多个玩家发牌
# method 2:
deck = []
create_deck(deck)
shuffle_deck(deck)

p1_deck = []
p2_deck = []
p3_deck = []
p4_deck = []
p5_deck = []
deal_to_multi_players(
    deck, p1_deck, p2_deck, p3_deck, p4_deck, p5_deck)

record_deck(p1_deck, 'P1.txt')
record_deck(p2_deck, 'P2.txt')
record_deck(p3_deck, 'P3.txt')
record_deck(p4_deck, 'P4.txt')
record_deck(p5_deck, 'P5.txt')
