### HighScores Module  ###
## S Forrest 09/02/2014 ##

class Score(object):
    def __init__(self, plr, score):
        self.plr = plr
        self.scr = score
    def __getitem__(self, index):
        if index == 0:
            return self.scr
        elif index == 1:
            return self.plr
        else:
            raise IndexError
    def __str__(self):
        return self.plr + ":" + str(self.scr)

class ScoreTable(object):
    def __init__(self):
        self.scores = list()
        self.positions = dict()

    def AddScore(self,score):
        self.scores.append(score)
        self.__sort()
        
    def __sort(self):
        ##uses a basic bubble sort algorithm
        for passnum in range(len(self.scores)-1,0,-1):
            for i in range(passnum):
                if self.scores[i][0] > self.scores[i+1][0]:
                    temp = self.scores[i]
                    self.scores[i] = self.scores[i+1]
                    self.scores[i+1] = temp

    def __pos(self):
        self.positions = dict()
        position = len(self.scores)
        for i in range(len(self.scores)):
            self.positions[position] = self.scores[i]
            position -= 1

    def __str__(self):
        self.__pos()
        returnstring = ''
        for key in self.positions.keys():
            returnstring += (str(key) +' '+ str(self.positions[key]) + '\n')
            
        return returnstring
        
if __name__ == '__main__':
    HIGHSCORES = ScoreTable()
    for i in range(5):
        name = raw_input('Name: ')
        rawscore = int(raw_input("Score: "))
        scoreobj = Score(name,rawscore)
        HIGHSCORES.AddScore(scoreobj)
    print HIGHSCORES
                    
