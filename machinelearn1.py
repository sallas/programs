import string
import random
class AI(object):
    def __init__(self, games = 0):
        if games == 0:
            self.games = {1:[1.0,1.0],2:[1.0,1.0]}
        else:
            self.games = games
    def get_games(self):
        return self.games
    def get_wins(self, key):
        return self.games[key][0]
    def get_loses(self, key):
        return self.games[key][1]
    def win(self, choice):
        self.games[choice][0] += 1
        print 'win'
    def lose(self, choice):
        self.games[choice][1] += 1
        print 'lose'
        
             


def game():
    win = 0.0
    total = 0.0
    computer = AI()
    for i in xrange(100):
        player = random.choice([1,1,2,2])
        
        choice_dict = dict()
        
        for d in computer.games:
            choice_dict[d] = computer.get_wins(d)/computer.get_loses(d)
        print choice_dict
        choice_list = sorted(choice_dict, key=choice_dict.__getitem__,reverse=True)
        print choice_list
        AIchoice = choice_list[0]
        
        #AIchoice = random.choice([1, 2])
        if player == AIchoice:
            computer.win(AIchoice)
            win += 1
        else:
            computer.lose(AIchoice)
        total += 1
    print computer.games
    return (win/total)*100
