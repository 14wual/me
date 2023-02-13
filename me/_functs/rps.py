# ██╗    ██╗██╗   ██╗ █████╗ ██╗     
# ██║    ██║██║   ██║██╔══██╗██║     
# ██║ █╗ ██║██║   ██║███████║██║     (code by wual)
# ██║███╗██║██║   ██║██╔══██║██║     
# ╚███╔███╔╝╚██████╔╝██║  ██║███████╗
#  ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝
# See proyect >> https://github.com/14wual/me
# Follow me >> https://twitter.com/codewual

# Based on: https://github.com/14wual/Random-Scripts/blob/main/Scripts/2022/Others/RockPaperScissors.py

# --------------------Extern Imports--------------------
import random
import sys

# --------------------Intern Imports--------------------
from _app.main import MeAPP

# --------------------APP--------------------
class RPS:
    
    def __init__(self, meapp):
        self.meapp = MeAPP
        
        self.round = 0
        self.marker_player = 0
        self.marker_computer = 0
        
        self._round_event()
        
    def display_info(self):
        print("Round Number %d" % self.round)
        print(f"\nMarker {self.marker_player} (Player) - {self.marker_computer} (Computer)")
        print("Stone, Paper or Scissors?")
        
    def play(self, player):
        lists = ['Scissors','Paper','Stone']
        computer = random.choice(lists)
        
        if player == 'Scissors' or player == 'scissors':
            self.round += 1
            if computer == 'Scissors':print("Player TIE")
            elif computer == 'Paper':print("Player WIN");self.marker_player += 1
            elif computer == 'stone':print("Player LOSE");self.marker_computer += 1
        elif player == 'Stone' or player == 'stone':
            self.round += 1
            if computer == 'Scissors':print("Player WIN");self.marker_player += 1
            elif computer == 'Paper':print("Player LOSE");self.marker_computer += 1
            elif computer == 'stone':print("Player TIE")
        elif player == 'Paper' or player == 'paper':
            self.round += 1
            if computer == 'Scissors':print("Player LOSE");self.marker_computer += 1
            elif computer == 'Paper':print("Player TIE")
            elif computer == 'stone':print("Player WIN");self.marker_player += 1
        else:print("Invalid choose")
            
        self._round_event()
        
    def _round_event(self):
        RPS.display_info(self)
        choose = input("\n([Q] to exit) | Choose: ")

        if choose == "q" or choose == "Q":
            RPS.do_exit(self)
            sys.exit()
        else:RPS.play(self, choose)
    
    def do_exit(self):
        print("Round Number %d" % self.round)
        print(f"\nMarker {self.marker_player} (Player) - {self.marker_computer} (Computer)")
        print("\nBYE!")
        
