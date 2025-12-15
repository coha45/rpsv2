import random

class Game:
    choices = {
        "rock" : "scissors",
        "scissors" : "paper",
        "paper" : "rock",
    }
    def __init__(self, controller):
        self.controller = controller
        self.cur_rounds = self.controller.rounds
        self.over = False
        self.debounce = False   
        self.overall_wins = 0
        self.overall_losses = 0

    def advance_round(self):
        if self.cur_rounds <= 0: return
        
        self.cur_rounds -= 1
        if self.cur_rounds <= 0:            
            self.over = True

    def get_rand(self):
        return random.choice(list(self.choices.keys()))


    def determine_winner(self, choice, ai_choice):
        if self.over: return 

        if self.choices[choice] == ai_choice: # Win
            self.overall_wins += 1
            return 0
        elif self.choices[ai_choice] == choice: # Lose
            self.overall_losses += 1
            return 1
        else: # Draw
            return 2
        