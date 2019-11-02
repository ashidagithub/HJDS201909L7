# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.7.10

# Description:
# 洗牌机模块之一，可以
#   1) 创建一副标准的 54张牌
#   2) 将这副牌随机洗好
#   3) 可以将一副牌的内容记录到一个指定的文件里
# ------------------------(max to 80 columns)-----------------------------------

# import some external moduls
import random
import codecs
import copy
import os

# initialize var
cardJokers = ('♞', '♘')
cardMarks = ('♠', '♥', '♣', '♦')
cardNumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'J', 'Q', 'K', 'A')


def create_deck(new_deck):
    'Desc: Make a new standard 54 cards poker, put them in order'
    for c in cardJokers:
        new_deck.append(c)

    # add 4x13 cards
    for cn in cardNumbers:
        for cm in cardMarks:
            #card = cm + cn
            card = cn + cm
            new_deck.append(card)

    # shuffle_deck(new_deck)
    return


def shuffle_deck(deck):
    'Desc: Shuffle a deck'
    #shuffledDeck = copy.copy(deck)
    random.shuffle(deck)
    return


def record_deck(deck, filename):
    'Desc: Write a deck into a specified file'
    out_path = os.getcwd() + '\\output_decks\\' + filename
    f = codecs.open(out_path, "w", "utf-8")
    for card in deck:
        f.write(card)
        f.write('\n')
    f.close()
    return
