import random
import time

card = ('Ace of Clubs', 'Ace of Spades', 'Ace of Hearts', 'Ace of Diamonds', '2 of Clubs', '2 of Spades', '2 of Hearts', '2 of Diamonds', '3 of Clubs', '3 of Spades', '3 of Hearts', '3 of Diamonds', '4 of Clubs', '4 of Spades', '4 of Hearts', '4 of Diamonds', '5 of Clubs', '5 of Spades', '5 of Hearts', '5 of Diamonds', '6 of Clubs', '6 of Spades', '6 of Hearts', '6 of Diamonds', '7 of Clubs', '7 of Spades', '7 of Hearts', '7 of Diamonds', '8 of Clubs', '8 of Spades', '8 of Hearts', '8 of Diamonds', '9 of Clubs', '9 of Spades', '9 of Hearts', '9 of Diamonds', '10 of Clubs', '10 of Spades', '10 of Hearts', '10 of Diamonds', 'Jack of Clubs', 'Jack of Spades', 'Jack of Hearts', 'Jack of Diamonds', 'Queen of Clubs', 'Queen of Spades', 'Queen of Hearts', 'Queen of Diamonds', 'King of Clubs', 'King of Spades', 'King of Hearts', 'King of Diamonds')

def card_function():
  if card == 'Ace of Clubs':
    if random.choice(card) == player_random:
      if player_number <= 11:
        player_number += 10
      else:
        player_number += 1
    elif random.choice(card) == ai_random:
      if ai_number <= 11:
        ai_number += 10
      else:
        ai_number += 1

  if card == 'Ace of Spades':
    if random.choice(card) == player_random:
      if player_number <= 11:
        player_number += 10
      else:
        player_number += 1
    elif random.choice(card) == ai_random:
      if ai_number <= 11:
        ai_number += 10
      else:
        ai_number += 1

  if card == 'Ace of Hearts':
    if random.choice(card) == player_random:
      if player_number <= 11:
        player_number += 10
      else:
        player_number += 1
    elif random.choice(card) == ai_random:
      if ai_number <= 11:
        ai_number += 10
      else:
        ai_number += 1

  if card == 'Ace of Diamonds':
    if random.choice(card) == player_random:
      if player_number <= 11:
        player_number += 10
      else:
        player_number += 1
    elif random.choice(card) == ai_random:
      if ai_number <= 11:
        ai_number += 10
      else:
        ai_number += 1

  if card == '2 of Clubs':
    if random.choice(card) == player_random:
      player_number += 2
    elif random.choice(card) == ai_random:
      ai_number += 2

  if card == '2 of Spades':
    if random.choice(card) == player_random:
      player_number += 2
    elif random.choice(card) == ai_random:
      ai_number += 2

  if card == '2 of Hearts':
    if random.choice(card) == player_random:
      player_number += 2
    elif random.choice(card) == ai_random:
      ai_number += 2

  if card == '2 of Diamonds':
    if random.choice(card) == player_random:
      player_number += 2
    elif random.choice(card) == ai_random:
      ai_number += 2

  if card == '3 of Clubs':
    if random.choice(card) == player_random:
      player_number += 3
    elif random.choice(card) == ai_random:
      ai_number += 3

  if card == '3 of Spades':
    if random.choice(card) == player_random:
      player_number += 3
    elif random.choice(card) == ai_random:
      ai_number += 3

  if card == '3 of Hearts':
    if random.choice(card) == player_random:
      player_number += 3
    elif random.choice(card) == ai_random:
      ai_number += 3

  if card == '3 of Diamonds':
    if random.choice(card) == player_random:
      player_number += 3
    elif random.choice(card) == ai_random:
      ai_number += 3

  if card == '4 of Clubs':
    if random.choice(card) == player_random:
      player_number += 4
    elif random.choice(card) == ai_random:
      ai_number += 4

  if card == '4 of Spades':
    if random.choice(card) == player_random:
      player_number += 4
    elif random.choice(card) == ai_random:
      ai_number += 4

  if card == '4 of Hearts':
    if random.choice(card) == player_random:
      player_number += 4
    elif random.choice(card) == ai_random:
      ai_number += 4

  if card == '4 of Diamonds':
    if random.choice(card) == player_random:
      player_number += 4
    elif random.choice(card) == ai_random:
      ai_number += 4

  if card == '5 of Clubs':
    if random.choice(card) == player_random:
      player_number += 5
    elif random.choice(card) == ai_random:
      ai_number += 5

  if card == '5 of Spades':
    if random.choice(card) == player_random:
      player_number += 5
    elif random.choice(card) == ai_random:
      ai_number += 5

  if card == '5 of Hearts':
    if random.choice(card) == player_random:
      player_number += 5
    elif random.choice(card) == ai_random:
      ai_number += 5

  if card == '5 of Diamonds':
    if random.choice(card) == player_random:
      player_number += 5
    elif random.choice(card) == ai_random:
      ai_number += 5

  if card == '6 of Clubs':
    if random.choice(card) == player_random:
      player_number += 6
    elif random.choice(card) == ai_random:
      ai_number += 6

  if card == '6 of Spades':
    if random.choice(card) == player_random:
      player_number += 6
    elif random.choice(card) == ai_random:
      ai_number += 6

  if card == '6 of Hearts':
    if random.choice(card) == player_random:
      player_number += 6
    elif random.choice(card) == ai_random:
      ai_number += 6

  if card == '6 of Diamonds':
    if random.choice(card) == player_random:
      player_number += 6
    elif random.choice(card) == ai_random:
      ai_number += 6

  if card == '7 of Clubs':
    if random.choice(card) == player_random:
      player_number += 7
    elif random.choice(card) == ai_random:
      ai_number += 7

  if card == '7 of Spades':
    if random.choice(card) == player_random:
      player_number += 7
    elif random.choice(card) == ai_random:
      ai_number += 7

  if card == '7 of Hearts':
    if random.choice(card) == player_random:
      player_number += 7
    elif random.choice(card) == ai_random:
      ai_number += 7

  if card == '7 of Diamonds':
    if random.choice(card) == player_random:
      player_number += 7
    elif random.choice(card) == ai_random:
      ai_number += 7

  if card == '8 of Clubs':
    if random.choice(card) == player_random:
      player_number += 8
    elif random.choice(card) == ai_random:
      ai_number += 8

  if card == '8 of Spades':
    if random.choice(card) == player_random:
      player_number += 8
    elif random.choice(card) == ai_random:
      ai_number += 8

  if card == '8 of Hearts':
    if random.choice(card) == player_random:
      player_number += 8
    elif random.choice(card) == ai_random:
      ai_number += 8

  if card == '8 of Diamonds':
    if random.choice(card) == player_random:
      player_number += 8
    elif random.choice(card) == ai_random:
      ai_number += 8

  if card == '9 of Clubs':
    if random.choice(card) == player_random:
      player_number += 9
    elif random.choice(card) == ai_random:
      ai_number += 9

  if card == '9 of Spades':
    if random.choice(card) == player_random:
      player_number += 9
    elif random.choice(card) == ai_random:
      ai_number += 9

  if card == '9 of Hearts':
    if random.choice(card) == player_random:
      player_number += 9
    elif random.choice(card) == ai_random:
      ai_number += 9

  if card == '9 of Diamonds':
    if random.choice(card) == player_random:
      player_number += 9
    elif random.choice(card) == ai_random:
      ai_number += 9

  if card == '10 of Clubs':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == '10 of Spades':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == '10 of Hearts':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == '10 of Diamonds':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'Jack of Clubs':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'Jack of Spades':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'Jack of Hearts':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'Jack of Diamonds':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'Queen of Clubs':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'Queen of Spades':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'Queen of Hearts':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'Queen of Diamonds':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'King of Clubs':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'King of Spades':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'King of Hearts':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

  if card == 'King of Diamonds':
    if random.choice(card) == player_random:
      player_number += 10
    elif random.choice(card) == ai_random:
      ai_number += 10

games_played=0
games_won=0
games_lost=0
name = input("Hello and welcome to Blackjack, what is your name? ")
#decks = input("How many decks would you like to play Blackjack with?") totalcards = cards*decks
while 0 == 0 :
  player_number=0
  player_list = []
  ai_number=0
  ai_list = []
  pass_confirmation = 'no'
  while player_number<21 or pass_confirmation == 'no':
    decision = input(f"Would you like to hit or pass {name}? ")
    if decision == 'hit':
      player_random = random.choice(card)
      card_function()
      player_list += player_random
      print(f"You have been hit with a {player_random}.")
    elif decision == 'pass':
      while 0 == 0:
        pass_confirmation = input(f"Are you sure you want to pass {name}? You have the cards: {player_list} which adds up to {player_number}. ")
        if pass_confirmation == 'yes':
          print("Ok, you have passed.")
          break
        elif pass_confirmation == 'no':
          print("You have aborted the passing-process")
          break
        else:
          print ("Please respond with either 'yes' or 'no'.")
    else:
      print("Please type in either 'hit' or 'pass'.")
  while ai_number<21 or ai_number<player_number:
    ai_random = random.choice(card)
    card_function()
    ai_list += ai_random
  print("Ok, you have the cards: {player_list} which adds up to {player_number}. The computer has the cards: {ai_list} which adds up to {ai_number}. And the winner is...")
  time.sleep(1)
  if player_number>=21 or player_number<ai_number and ai_number<=21:
    games_lost += 1
    print(f"The computer! Sorry {name}, you lost this game.")
  elif player_number<=21 and player_number>ai_number or ai_number>=21:
    games_won += 1
    print(f"{name}! Congratulations you won this game of blackjack!")
  else:
    print("You have tied")
  replay = input("Would you like to play again?")
  if replay == 'no':
    games_played += 1
    break
  elif replay == 'yes':
    games_played += 1
    print("Ok, another game it is then")
  else:
    print("Please either respond with 'yes' or 'no'.")

print(f"Thank you {name} for playing my game {games_played} many times! You won {games_won} of the games and lost {games_lost} of them.")