import random
# PCの手
P_hand = [1,2,3]

def cpu_pon():
    pc = P_hand[random.randint(0,2)]
    if pc == 1:
        print('グー')
    elif pc == 2:
        print('チョキ')
    else:
        print('パー')