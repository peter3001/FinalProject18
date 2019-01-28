import random #Random is imported and used for choosing a random card
import time #Time is imported to later have a sleep command to add suspense

card = {'Ace of Clubs': 1, 'Ace of Spades': 1, 'Ace of Hearts': 1, 'Ace of Diamonds': 1, '2 of Clubs': 2, '2 of Spades': 2, '2 of Hearts': 2, '2 of Diamonds': 2, '3 of Clubs': 3, '3 of Spades': 3, '3 of Hearts': 3, '3 of Diamonds': 3, '4 of Clubs': 4, '4 of Spades': 4, '4 of Hearts': 4, '4 of Diamonds': 4, '5 of Clubs': 5, '5 of Spades': 5, '5 of Hearts': 5, '5 of Diamonds': 5, '6 of Clubs': 6, '6 of Spades': 6, '6 of Hearts': 6, '6 of Diamonds': 6, '7 of Clubs': 7, '7 of Spades': 7, '7 of Hearts': 7, '7 of Diamonds': 7, '8 of Clubs': 8, '8 of Spades': 8, '8 of Hearts': 8, '8 of Diamonds': 8, '9 of Clubs': 9, '9 of Spades': 9, '9 of Hearts': 9, '9 of Diamonds': 9, '10 of Clubs': 10, '10 of Spades': 10, '10 of Hearts': 10, '10 of Diamonds': 10, 'Jack of Clubs': 10, 'Jack of Spades': 10, 'Jack of Hearts': 10, 'Jack of Diamonds': 10, 'Queen of Clubs': 10, 'Queen of Spades': 10, 'Queen of Hearts': 10, 'Queen of Diamonds': 10, 'King of Clubs': 10, 'King of Spades': 10, 'King of Hearts': 10, 'King of Diamonds': 10}
#The huge list above has every card in a normal deck and gives them the proper value they are supposed to have. The aces have been set to have the value of only 1 instead of 1 or 11.

games_played = 0 #The total games that have been played
games_won = 0 #Total games won
games_lost = 0 #Total games lost
games_tied = 0 # Total games tied
name = input("Hello, and welcome to Blackjack. What is your name? ") #Asks player for their name, and player is referred to by name
replay = 'yes' #Replay is set to be equal to 'yes' so that the huge while loop below functions properly.
while replay[0] == 'y': #This massive while loop gives the game replayability. As long as replay starts with the letter 'y' the game can be replayed
  player_number = 0
  #Above is the value the player has once all the cards are added up
  player_list = [] #This is a list of all the cards the player has been hit with.
  ai_number = 0 #This is the value that the AI has once cards are added.
  ai_list = [] #This is a list of all the cards the AI has been hit with.
  pass_confirmation = 'no' #The pass confirmation is set to 'no' so that the while loop below works
  while (player_number < 21 or pass_confirmation == 'no'): #This while loop is to allow the player to make the hit or pass decision.
    if player_number > 21: #If the player's total value is greater than 21:
      print()
      print("Your amount has exceeded 21. You have automatically passed.") #The player is told their amount is greater than 21, which means they have automatically lost the game.
      time.sleep(3) #There is a 3 second pause for the player to realize they have just lost the game.
      print()
      break #The hit or pass decision loop is broken
    if player_number == 21: #If the player's total is equal to 21:
      print()
      print("Your amount is 21. You have automatically passed.") #The player is told their amount has reached the lucky number of 21, and they can not hit so they automatically pass.
      time.sleep(3) #There is a 3 second pause for the player to realize they have very good luck and have just won the game.
      print()
      break #The loop is broken
    print()
    decision = input(f"Would you like to hit or pass {name}? ") #Player is told if they wish to hit or pass
    if decision == 'hit': #If the decision is hit:
      card_choosing = {
        1: 'Ace of Clubs',
        2: 'Ace of Spades',
        3: 'Ace of Hearts',
        4: 'Ace of Diamonds',
        5: '2 of Clubs',
        6: '2 of Spades',
        7: '2 of Hearts',
        8: '2 of Diamonds',
        9: '3 of Clubs',
        10: '3 of Spades',
        11: '3 of Hearts',
        12: '3 of Diamonds',
        13: '4 of Clubs',
        14: '4 of Spades',
        15: '4 of Hearts',
        16: '4 of Diamonds',
        17: '5 of Clubs',
        18: '5 of Spades',
        19: '5 of Hearts',
        20: '5 of Diamonds',
        21: '6 of Spades',
        22: '6 of Clubs',
        23: '6 of Hearts',
        24: '6 of Diamonds',
        25: '7 of Clubs',
        26: '7 of Spades',
        27: '7 of Hearts',
        28: '7 of Diamonds',
        29: '8 of Clubs',
        30: '8 of Spades',
        31: '8 of Hearts',
        32: '8 of Diamonds',
        33: '9 of Clubs',
        34: '9 of Spades',
        35: '9 of Hearts',
        36: '9 of Diamonds',
        37: '10 of Clubs',
        38: '10 of Spades',
        39: '10 of Hearts',
        40: '10 of Diamonds',
        41: 'Jack of Clubs',
        42: 'Jack of Spades',
        43: 'Jack of Hearts',
        44: 'Jack of Diamonds',
        45: 'Queen of Clubs',
        46: 'Queen of Spades',
        47: 'Queen of Hearts',
        48: 'Queen of Diamonds',
        49: 'King of Clubs',
        50: 'King of Spades',
        51: 'King of Hearts',
        52: 'King of Diamonds'}
      #This massive list is used to randomly select one of cards from the first list. The reason this list was made was due to complications from randomly selecting a card directly from the first list. This problem was solved by this list, which gives each of the 52 cards a number from 1-52, and then one of the numbers is randomly selected to choose that card

      player_random = random.randint(1, 52) #A random number from 1 to 52 is selected and designated as 'player_random'
      player_card = card_choosing[player_random] #The number that was randomly selected is then checked on the 'card_choosing' list to select the proper card. That card is then set equal to 'player_card'
      player_number += int(card[player_card]) #The card 'player_card' is then searched under the 'card' list to find the value it is set to. That value is added to 'player_number'
      player_list.append(str(player_card)) #The card itself is added to 'player_list' so that the player can see what exact card they have been given
      print()
      print(f"You have been hit with {player_card}.") #The player is told what card they have been given
      print("You have: " + str(player_list) + " which equals " + str(player_number)) #The player is told all the cards they have at the moment, and the value all those cards add up to

    elif decision == 'pass': #If the player decides to pass:
      pass_confirmation = input(f"Are you sure you want to pass {name}? You have the cards: {player_list} which add up to {player_number}. ") #The player is asked if they really want to pass, and is reminded of what cards they have and the value it adds up to
      pass_confirmation = pass_confirmation.lower() #the answer given sets the letters to lowercase
      if pass_confirmation[0] == 'y' or pass_confirmation[0] == 'n': #If the answer the player has given starts with either 'y' or 'n':
        if pass_confirmation[0] == 'y': #If the answer starts with 'y':
          print()
          print("You passed.") #The player is told they have passed
          print()
          break #The hit or pass loop is broken
        elif pass_confirmation[0] == 'n': #if the answer starts with 'n':
          print("You have aborted the passing-process") #The player is told they have decided not to pass
      else: #If there is an answer that doesn't start with 'y' or 'n':
        print("The passing-process has been aborted due to an incorrect input. Please type in either 'yes' or 'no' when trying to pass.") #The player is told they have given an incorrect answer, and the passing process is aborted
    else: #If the player does not respond with 'hit' or 'pass':
      print("Please type in either 'hit' or 'pass'.") #They are told to do so

  while ai_number < 21: #The AI will repeatedly hit as long as the AI's cards have a total value less than 21
    if ai_number > player_number: #If the AI gets a higher value than the player:
      break #The loop breaks and the AI stops getting cards
    elif player_number > 21: #If the player has already lost by getting more than 21:
      break #The AI does not draw any cards, and the loop breaks
    ai_random = random.randint(0, 52) #The same process for selecting a random card for the player is done for the AI. A random number from 1 to 52 is selected and designated as 'ai_random'
    ai_card = card_choosing[ai_random] #The number that was randomly selected is then checked on the 'card_choosing' to select the proper card. That card is then set equal to 'ai_card'
    ai_number += int(card[ai_card]) #The card 'ai_card' is then searched under the 'card' list to find the value it is set to. That value is added to 'ai_number'
    ai_list.append(str(ai_card)) #The card itself is added to 'ai_list' so that the player can see what exact card the AI has been given

  print(f"You have the cards: {player_list} which add up to {player_number}. The computer has the cards: {ai_list} which add up to {ai_number}. And the winner is...") #Both the player's and AI's cards and values are listed
  time.sleep(3) #There is a 3 second delay to add dramatic effect

  if player_number == ai_number: #If they player's and AI's values have managed to end up equal to each other:
    games_tied += 1 #The player ties with the AI and it is recorded
    print("You and the computer have tied!") #The player is told they have managed to tie
  elif player_number > 21 or player_number < ai_number and ai_number <= 21:#If the player has more than 21 or the AI has more than the player and a value less than or equal to 21:
    games_lost += 1 #They lose and it is recorded
    print(f"The computer! Sorry {name}, you lost this game.") #Player is told they just lost the game
  elif player_number <= 21 and player_number > ai_number or ai_number >= 21: #If the situation is flipped:
    games_won += 1 #The player wins and it is recorded
    print(f"{name}! Congratulations you won this game of blackjack!") #The player is told they won the game


  while 0 == 0: #While loop to make sure the player gives a valid answer for whether they want to replay
    print()
    print()
    replay = input("Would you like to play again? ") #Player is asked if they want to replay the game or not
    replay = replay.lower() #The answer given is made into lowercase letters
    if replay[0] == 'n': #If the response ends with the letter 'n':
      games_played += 1 #The total games played is added by one
      break #This while loop is broken, and so is the replayability while loop due to replay now being equal to a word that doesn't start with 'y'
    elif replay[0] == 'y': #If the response ends with the letter 'y':
      games_played += 1 #The total games played is added by one
      print("Ok, another game it is then.") #The player is told another game is about to begin
      print()
      print()
      player_number = 0 #Player's value is reset
      player_list = [] #Player's list is reset
      ai_number = 0 #AI's value is reset
      ai_list = [] #AI's list is reset
      pass_confirmation = 'no' #Pass confirmation is set to 'no' to prevent any possible complications
      break #This while loop is broken, but not the replayability while loop due to replay still being equal to a word that starts with 'y'
    else: #If the player gives an invalid answer:
      print("Please either respond with 'yes' or 'no'.") #The player is told to give a valid answer

print()
print(f"Thank you {name} for playing my game {games_played} times! You won {games_won} of the games, lost {games_lost} of the games, and tied {games_tied} of the games.") #Player is thanked for playing game, and given their results