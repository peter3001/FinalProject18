cards = ('Ace of Clubs', 'Ace of Spades', 'Ace of Hearts', 'Ace of Diamonds'== ace,

'2 of Clubs', '2 of Spades', '2 of Hearts', '2 of Diamonds':{
2card = 2
}
'3 of Clubs', '3 of Spades', '3 of Hearts', '3 of Diamonds':{
3card = 3
}
'4 of Clubs', '4 of Spades', '4 of Hearts', '4 of Diamonds':{
4card = 4
}
'5 of Clubs', '5 of Spades', '5 of Hearts', '5 of Diamonds':{
5card = 5
}
'6 of Clubs', '6 of Spades', '6 of Hearts', '6 of Diamonds':{
6card = 6
'7 of Clubs', '7 of Spades', '7 of Hearts', '7 of Diamonds':{
7card = 7
}
'8 of Clubs', '8 of Spades', '8 of Hearts', '8 of Diamonds':{
8card = 8
}
'9 of Clubs', '9 of Spades', '9 of Hearts', '9 of Diamonds':{
9card = 9
}
'10 of Clubs', '10 of Spades', '10 of Hearts', '10 of Diamonds':{
10card = 10
}
'Jack of Clubs', 'Jack of Spades', 'Jack of Hearts', 'Jack of Diamonds':{
Jack = 10
}
'Queen of Clubs', 'Queen of Spades', 'Queen of Hearts', 'Queen of Diamonds':{
Queen = 10
}
'King of Clubs', 'King of Spades', 'King of Hearts', 'King of Diamonds':{
King = 10
})
if 11+x<=21:
  ace = 11
else:
  ace = 1

name = input("Hello and welcome to Blackjack, what is your name?")
decks = input("How many decks would you like to play Blackjack with?")
cards * decks
while 0 == 0 :
  random.select cards
  print(f"Would you like to hit or pass {name}?")
  while winning <