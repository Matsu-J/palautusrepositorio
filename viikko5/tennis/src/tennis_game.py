class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.scores = {
            self.player1: 0,
            self.player2: 0
        }

    def won_point(self, player_name):
        self.scores[player_name] += 1

    def even(self, score):
        if score >= 3:
            score = 3
        even_score_labels = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
        return even_score_labels[score]
    def advantage(self):
        difference = self.scores[self.player1] - self.scores[self.player2]
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
    def scoreboard(self):
        scores = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{scores[self.scores[self.player1]]}-{scores[self.scores[self.player2]]}"

    def get_score(self):
        if self.scores[self.player1] == self.scores[self.player2]:
            return self.even(self.scores[self.player1])
        elif self.scores[self.player1] >= 4 or self.scores[self.player2] >= 4:
            return self.advantage()
        else:
            return self.scoreboard()

