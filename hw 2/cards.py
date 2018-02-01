import random
import unittest

# SI 206 Winter 2018
# Homework 2 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: Wednesday 4-5:30
# People you worked with:

######### DO NOT CHANGE PROVIDED CODE #########
### Below is the same cards.py code you saw in lecture.
### Scroll down for assignment instructions.
#########

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] # forming an empty list
		for c in self.cards: # each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
		if card.__str__() not in card_strs: # if the string representing this card is not in the list already
			self.cards.append(card) # append it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)


def play_war_game(testing=False):
	# Call this with testing = True and it won't print out all the game stuff -- makes it hard to see test results
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()
	if not testing:
		print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()
		print('p1 rank_num=', p1_card.rank_num, 'p2 rank_num=', p2_card.rank_num)
		if not testing:
			print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:

			if not testing:
				print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			if not testing:
				print("Player 2 wins a point!")
			p2_score += 1
		else:
			if not testing:
				print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


######### DO NOT CHANGE CODE ABOVE THIS LINE #########

## You can write any additional debugging/trying stuff out code in this section...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

#########







##**##**##**##@##**##**##**## # DO NOT CHANGE OR DELETE THIS COMMENT LINE -- we use it for grading your file
###############################################

### Write unit tests below this line for the cards code above.

class TestCard(unittest.TestCase):


	# this is a "test"
	def test_create(self):
		card1 = Card()
		self.assertEqual(card1.suit, "Diamonds")
		self.assertEqual(card1.rank, 2)

#1. Test that if you create a card with rank 12, its rank will be "Queen"
class Problem1(unittest.TestCase):
	def test1(self):
		queen = Card(0, 12)
		self.assertEqual(str(queen), "Queen of Diamonds", "Checking you create a card with rank 12, its rank will be Queen")

#2. Test that if you create a card with rank 1, its rank will be "Ace"
class Problem2(unittest.TestCase):
	def test2(self):
		ace = Card(0,1)
		self.assertEqual(str(ace), "Ace of Diamonds", "you create a card with rank 1, its rank will be Ace")

#3. Test that if you create a card instance with rank 3, its rank will be 3
class Problem3(unittest.TestCase):
	def test3(self):
		three = Card(0, 3)
		self.assertEqual(three.rank, 3, "Checking you create a card instance with rank 3, its rank will be 3")

#4. Test that if you create a card instance with suit 1, it will be suit "Clubs"
class Problem4(unittest.TestCase):
	def test4(self):
		clubs = Card(1)
		self.assertEqual(str(clubs), "2 of Clubs", "Checking you create a card instance with suit 1, it will be suit Clubs")

#5. Test that if you create a card instance with suit 2, it will be suit "Hearts"
class Problem5(unittest.TestCase):
	def test5(self):
		clubs = Card(2)
		self.assertEqual(clubs.suit, "Hearts")

#6. Test that if you create a card instance, it will have access to a variable suit_names that contains the list ["Diamonds","Clubs","Hearts","Spades"]
class Problem6(unittest.TestCase):
	def test6(self):
		clubs = Card(1)
		self.assertEqual(clubs.suit_names,["Diamonds","Clubs","Hearts","Spades"])

#7. Test that if you invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string "7 of Hearts"
class Problem7(unittest.TestCase):
	def test7(self):
		sevenHearts = Card(2,7)
		self.assertEqual(str(sevenHearts), "7 of Hearts", "Checking youyou invoke the __str__ method of a card instance that is created with suit=2, rank=7, it returns the string 7 of Hearts")

#8. Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"
class Problem8(unittest.TestCase):
	def test8(self):
		kingspades = Card(3,13)
		self.assertEqual(str(kingspades), "King of Spades", "Checking youyou invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string King of Spades")

#9. Test that if you create a deck instance, it will have 52 cards in its cards instance variable
class Problem9(unittest.TestCase):
	def test9(self):
		deck = Deck()
		self.assertEqual(len(deck.cards), 52, "Checking if card is right")

#10. Test that if you invoke the pop_card method on a deck, it will return a card instance.
class Problem10(unittest.TestCase):
	def test10(self):
		deck = Deck()
		self.assertEqual(type(deck.pop_card()), Card, "Checking if returning card instance")

#11. Test that if you invoke the pop_card method on a deck, the deck has one fewer cards in it afterwards.
class Problem11(unittest.TestCase):
	def test11(self):
		deck = Deck()
		pop=deck.pop_card()
		self.assertEqual(len(deck.cards), 51, "Checking if card is right")

#12. Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use pop_card function first to remove a card from the deck and then replace the same card back in)
class Problem12(unittest.TestCase):
	def test12(self):
		deck = Deck()
		pop=deck.pop_card()
		replace= deck.replace_card(pop)
		self.assertEqual(len(deck.cards), 52, "Checking if card is right")

#13. Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)
class Problem13(unittest.TestCase):
	def test13(self):
		deck = Deck()
		replace= deck.replace_card(Card(0,2))
		self.assertEqual(len(deck.cards), 52, "Checking if card is right")


#14.Test that the return value of the play_war_game function is a tuple with three elements, the first of which is a string. (This will probably require multiple test methods!)
class Problem14(unittest.TestCase):
	def test14(self):
		result= play_war_game(testing=True)
		self.assertEqual(type(result), tuple)
		self.assertEqual(type(result[0]), str)
		self.assertEqual(len(result), 3)

#15. (and 16)  Write at least 2 additional tests. Make sure to include a descriptive message in these two so we can easily see what you are testing!
class Problem15(unittest.TestCase): #testing if the second element of result is an integer
	def test15(self):
		result= play_war_game(testing=True)
		self.assertEqual(type(result[1]), int)
class Problem16(unittest.TestCase): #testing if the third element of result is an integer
	def test16(self):
		result= play_war_game(testing=True)
		self.assertEqual(type(result[2]), int)


#############
## The following is a line to run all of the tests you include:
if __name__ == "__main__":
	unittest.main(verbosity=2)
## verbosity 2 to see detail about the tests the code fails/passes/etc.
