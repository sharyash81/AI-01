import copy

import numpy as np

count_win = np.zeros(28)
count_lose = np.zeros(28)
win_strategy = []
lose_strategy = []

def create_game():
    global  count_win,count_lose,win_strategy
    count_win = np.zeros(28)
    count_lose = np.zeros(28)
    win_strategy = []
    # row_win
    for i in [0,1,5,6,10,11,15,16,20,21]:
        win_strategy.append([i,i+1,i+2,i+3])
    # col_win
    for i in range(10):
        win_strategy.append([i,i+5,i+10,i+15])
    # neg slope win
    for i in [0,1,5,6]:
        win_strategy.append([i,i+6,i+12,i+18])
    # pos slope win
    for i in [3,4,8,9]:
        win_strategy.append([i,i+4,i+8,i+12])
    global lose_strategy
    lose_strategy = copy.deepcopy(win_strategy)



def ai_action(game_state, player: list):
    update_win(player,False)
    update_lose(player,False)
    target = find_strategy(game_state)
    update_win([target], True)
    update_lose([target], True)
    return target


def find_strategy(game_state):
    maxW = max(count_win)
    maxL = max(count_lose)
    count_win_i = np.zeros(25)
    count_lose_i = np.zeros(25)
    for index,win in enumerate(win_strategy):
        if count_win[index] == maxW:
            for i in win :
                if game_state[i] == None :
                    count_win_i[i]+=1
    for index,lose in enumerate(lose_strategy):
        if count_lose[index] == maxL:
            for i in lose:
                if game_state[i] == None :
                    count_lose_i[i]+=1
    if maxL == 1 or maxW >= maxL :
        return attack(count_win_i,count_lose_i)
    else :
        return defend(count_win_i,count_lose_i)


def attack(count_win_i,count_lose_i):
    l = list()
    maxC = max(count_win_i)
    for i in range(len(count_win_i)):
        if count_win_i[i] == maxC:
            l.append(i)
    target = l[0]
    for i in l :
        if count_lose_i[i] > count_lose_i[target]:
            target = i
    return target

def defend(count_win_i,count_lose_i):
    l = list()
    maxC = max(count_lose_i)
    for i in range(len(count_lose_i)):
        if count_lose_i[i] == maxC:
            l.append(i)
    target = l[0]
    for i in l:
        if count_win_i[i] > count_lose_i[target]:
            target = i
    return target


def update_win(player: list , ai:bool):
    if not ai:
        for i in range(len(win_strategy)):
            if win_strategy[i].__contains__(player[-1]):
                count_win[i] = -1
    else :
        for i in range(len(win_strategy)):
            if win_strategy[i].__contains__(player[-1]) and count_win[i] != -1:
                count_win[i] += 1


def update_lose(player: list , ai):
    if not ai :
        for i in range(len(lose_strategy)):
            if lose_strategy[i].__contains__(player[-1]) and count_lose[i] != -1:
                count_lose[i] += 1
    else:
        for i in range(len(win_strategy)):
            if win_strategy[i].__contains__(player[-1]):
                count_lose[i] = -1









