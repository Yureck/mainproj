"""Example module for learning."""
import random


def get_choices():
   player_choice = input("Enter your choices (rock, paper, scissors): ")
   options = ["rock", "paper", "scissors"]
   computer_choice = random.choice(options)
   choices = {"player": player_choice, "computer": computer_choice}
   return choices

def check_winner(player, computer):
   print(f"computer {computer}")
   if player == computer:
       return "It's a tie!"
   elif (player == "rock" and computer == "scissors") or \
        (player == "scissors" and computer == "paper") or \
        (player == "paper" and computer == "rock"):
       return "You win!"
   else:
       return "You lose!"
  
choices = get_choices()
print(check_winner(choices["player"], choices["computer"]))
