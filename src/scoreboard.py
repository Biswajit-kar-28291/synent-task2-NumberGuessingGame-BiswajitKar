import json
import os

SCORE_FILE = "data/scores.json"


class Scoreboard:
    def __init__(self):
        self.scores = {
            "games_played": 0,
            "wins": 0,
            "losses": 0
        }
        self.load_scores()

    def load_scores(self):
        if os.path.exists(SCORE_FILE):
            with open(SCORE_FILE, "r") as file:
                self.scores = json.load(file)

    def save_scores(self):
        os.makedirs("data", exist_ok=True)

        with open(SCORE_FILE, "w") as file:
            json.dump(self.scores, file, indent=4)

    def update_score(self, won):
        self.scores["games_played"] += 1

        if won:
            self.scores["wins"] += 1
        else:
            self.scores["losses"] += 1

        self.save_scores()

    def show_scoreboard(self):
        print("\n========== SCOREBOARD ==========")
        print(f"Games Played : {self.scores['games_played']}")
        print(f"Wins         : {self.scores['wins']}")
        print(f"Losses       : {self.scores['losses']}")
        print("================================")