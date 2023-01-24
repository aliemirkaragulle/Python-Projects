# BlackJack Game

## Load Libraries
import random

## Classes

# Cards
# Face Cards (Jack, Queen, King) = 10
# Ace = 1 or 11 
suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

#### Card Class
class Card:
    def __init__(self, suits, ranks):
        self.suits = suits
        self.ranks = ranks
        self.value = values[ranks]

    # String Represenation of a Card 
    def __str__(self):
        return f"{self.ranks} of {self.suits}"

# Card Object
#two_of_hearts = Card("Hearts", "Two")
#print(two_of_hearts)

# Card Object Attributes
#print(two_of_hearts.suits)
#print(two_of_hearts.ranks)
#print(two_of_hearts.value)



# Deck Class
class Deck:
    def __init__(self):
        # Represenation of a Deck
        # 52 Cards (Objects) in a Deck (List)
        self.deck = []
        for suit in suits:
            for rank in ranks:
                #print(Card(suit, rank))
                self.deck.append(Card(suit, rank))
    
    # Shuffle the Deck
    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    # Remove the Last Card from a Deck
    def hit(self):
        return self.deck.pop(0)
    
    # Do Not Do an Action
    def stay(self):
        pass

    # String Representation of a Deck, including the number of cards
    def __str__(self):
        return f"The Deck has {len(self.deck)} cards."


# Deck Object
#game_deck = Deck()
#print(game_deck)

# Deck Attributes
#print(game_deck.deck[0])

# Check If hit() Method Works as Expected
"""
last_card = game_deck.hit()
print("A Card Has Been Dealt!")
print(game_deck)
print(f"Dealt Card: {last_card}")
"""

# Check If stay() Method Works as Expected
""" 
game_deck.stay()
print(game_deck)
"""

# Check If shuffle_deck() Method Works as Expected
"""
print(game_deck.deck[0])
game_deck.shuffle_deck()
print(game_deck.deck[0])
"""



# Hand Class (Base Class)
class Hand():
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_value = 0
    
    # Player's Hand's Total Value
    def update_hand_val(self):
        self.hand_value = 0
        for i in range(len(self.hand)):
            self.hand_value += self.hand[i].value

    def score(self):
        return self.hand_value
    
    def __str__(self):
        return f"{self.name} Hand Worth: {self.hand_value} & Number of Cards in Hand: {len(self.hand)}"

# Hand Object
#human_hand = Hand("Esiss")
#print(human_hand)

# Hand Methods
# Check If update_hand_val() Method Works as Expected
""" 
print(human_hand)
for i in range(4):
    print(game_deck.deck[i])
    human_hand.hand.append(game_deck.deck[i])
human_hand.update_hand_val()
print(human_hand)
"""

# Check If score() Method Works as Expected
"""
print(human_hand.score())
"""



# Player Class (Derived Class)
class Player(Hand):
    def __init__(self, name, bank_roll):
        Hand.__init__(self, name)
        self.bank_roll = bank_roll
    
    def __str__(self):
        return f"Player {self.name} has ${self.bank_roll}."

# Player Object 
#human = Player("Esiss", 1000)
#print(human)

# Player Attributes
#print(human.name)
#print(human.bank_roll)

# Player Methods
# Check If update_hand_val() & score() Method Works as Expected
""" 
print(human.hand_value)
for i in range(4):
    print(game_deck.deck[i])
    human.hand.append(game_deck.deck[i])
human.update_hand_val()
print(human.hand_value)
"""



# Computer Class (Derived Class)
class Computer(Hand):
    def __init__(self, name = "Computer", bank_roll = 0):
        Hand.__init__(self, name)
        self.bank_roll = bank_roll
    
    def __str__(self):
        return f"I am a {self.name}. I have ${self.bank_roll}."

# Computer Object
#computer = Computer()
#print(computer)

# Computer Attributes
#print(computer.name)
#print(computer.hand_value)

# Player Methods
# Check If update_hand_val() & score() Method Works as Expected
""" 
print(computer.hand_value)
for i in range(4):
    print(game_deck.deck[i])
    computer.hand.append(game_deck.deck[i])
computer.update_hand_val()
print(computer.hand_value)
"""



## Game Logic
print("Welcome to the BlackJack Game! \n")

# Set the Players Up
human_hand = Hand("Esiss")
human = Player("Esiss", 1923)

computer_hand = Hand("Computer")
computer = Computer("Computer")

print(human)
print(human_hand)
print("\n")

print(computer)
print(computer_hand)
print("\n")

# Set a New Game Up
game_deck = Deck()
game_deck.shuffle_deck()

""" 
print(f"Number of Cards in the Deck: {len(game_deck.deck)}")
for i in range(52):
    print(game_deck.deck[i])
"""

# Play
round_num = 1

# Bet Amount
while True:
    try:
        bet = int(input("Bet: "))
    except:
        print("Bet Must be an Integer!")
    else:
        print(f"Successful Bet!")

    if bet <= human.bank_roll:
        human.bank_roll -= bet
        print(f"Round: {round_num} Bet: {bet} Human Bank Roll Remaining: {human.bank_roll}")
        break
    else:
        print(f"Current Bank Roll: {human.bank_roll} Attempted to Bet: {bet}")
print("\n")

# Give 2 Cards to Computer & Human
# Human Cards are Face Up While a Single Card is Face Up for the Computer
for i in range(2):
    human_hand.hand.append(game_deck.hit())
    computer_hand.hand.append(game_deck.hit())

for i in range(2): 
    print(f"Cards Dealt to Human: {human_hand.hand[i]}")
    #print(f"Cards Dealt to Computer: {computer_hand.hand[i]}")
print(f"Cards Dealt to Computer: {computer_hand.hand[0]}")
print(f"Cards Dealt to Computer: FACE DOWN")
print("\n")

# 4 Cards Have Been Dealt
#print(f"Number of Cards in the Deck: {len(game_deck.deck)}")

# Update the Hand Value
human_hand.update_hand_val()
computer_hand.update_hand_val()

print(f"Total Observable Value of Human Cards (2 Face Up): {human_hand.hand_value}")
#print(f"Total Observable Value of Computer Cards (2 Face Up): {computer_hand.hand_value}")

# Show 1 Face Up Card & It's Value
print(f"Total Observable Value of Computer Cards (1 Face Up & 1 Face Down): {computer_hand.hand[0].value}")

# Turns
print("\n")

# Human Turn
# 2 Actions: HIT or STAY
# Score is Finalized
human_score = 0
computer_score = 0

tie = False

human_turn = True
while human_turn:

    #BlackJack In the First Round Both Human & Computer
    if human_hand.hand_value == 21 and computer_hand.hand_value == 21:
        tie = True
        print("TIE! No one earns or loses!")
        break


    # BlackJack In the First Round
    if human_hand.hand_value == 21:
        print("BLACKJACK FOR HUMAN!")
        # Human Doubles His Money
        human.bank_roll += bet * 2
        print(f"Human Bank Roll: {human.bank_roll}")
        break

    round = input(("HIT or STAY? "))
   
    # If HIT
    if round.upper() == "HIT":
        print(("Human HIT!"))
        
        # Human Receives a New Card
        received_card = game_deck.hit()
        human_hand.hand.append(received_card)
        
        # A Card Has Been Dealt
        print(f"Human Receives the Card: {received_card}")
        
        # Print the Current Human Deck
        """ 
        for i in range(len(human_hand.hand)):
            print(human_hand.hand[i])
        """
        # Update the Value of Cards that the Human Has
        human_hand.update_hand_val()
        print(f"Updated Value of Human Cards: {human_hand.hand_value}")

        human_score = human_hand.score()
        
        # Check If the Human Has an Ace In His Hand
        for i in range(len(human_hand.hand)):
            # If the Human Has an Ace In His Hand and He Has Never Transformed It
            if human_hand.hand[i].ranks == "Ace" and human_hand.hand[i].value == 11:
                print((f"You Have an Ace In Your Hand! You Transformed Ace's Value of 11 to 1!"))
                human_hand.hand[i].value = 1
           
                # Update the Value of Cards that the Human Has
                human_hand.update_hand_val()
                print(f"Updated Value of Human Cards after Ace: {human_hand.hand_value}")

                human_score = human_hand.score()

        # BlackJack
        if human_score == 21:
            print("BLACKJACK FOR HUMAN!")
            # Human Doubles His Money
            human.bank_roll += bet * 2
            print(f"Human Bank Roll: {human.bank_roll}")
            break

        # If Human > 21
        if human_score > 21:
            print(f"Human Score: {human_score}")
            print("HUMAN BUSTS!")
            print("COMPUTER WINS!")

            # Computer Takes the Human's Money
            human.bank_roll -= bet
            computer.bank_roll += bet
            print(f"Human Bank Roll: {human.bank_roll} & Computer Bank Roll: {computer.bank_roll}")
            break
    # If STAY
    else:
        print("Human STAY!")

        #Final Human Score
        human_score = human_hand.score()
        print(f"Final Human Score: {human_score}")
        break



# Computer Turn
# If Computer < 21, Computer HITS Till: Beat the Player or Bust!
computer_turn = True
while computer_turn and (human_score < 21) and tie == False:
    
    # BlackJack In the First Round
    if computer_hand.hand_value == 21:
        print("BLACKJACK FOR COMPUTER!")
        # Computer Takes the Human's Money
        human.bank_roll -= bet
        computer.bank_roll += bet
        print(f"Human Bank Roll: {human.bank_roll} & Computer Bank Roll: {computer.bank_roll}")
        break
   
    # Computer Receives a New Card
    received_card = game_deck.hit()
    computer_hand.hand.append(received_card)
        
    # A Card Has Been Dealt
    print(f"Computer Receives the Card: {received_card}")
        
    # Print the Current Computer Deck
    for i in range(len(computer_hand.hand)):
        print(computer_hand.hand[i])
        
    # Update the Value of Cards that the Computer Has
    computer_hand.update_hand_val()
    print(f"Updated Value of Computer Cards: {computer_hand.hand_value}")
    
    computer_score = computer_hand.score()

    # BlackJack
    if computer_score == 21:
        print("BLACKJACK FOR COMPUTER!")
        # Computer Takes the Human's Money
        human.bank_roll -= bet
        computer.bank_roll += bet
        print(f"Human Bank Roll: {human.bank_roll} & Computer Bank Roll: {computer.bank_roll}")
        break 
    # If Computer Busts
    if computer_score > 21:
        print(f"Computer Score: {computer_score}")
        print("COMPUTER BUSTS!")
        print("HUMAN WINS!")

        # Human Doubles His Money
        human.bank_roll += bet * 2
        print(f"Human Bank Roll: {human.bank_roll}")
        break

    # If Computer Beats Human
    if computer_score > human_score:
        print(f"Computer Score: {computer_score} & Human Score: {human_score}")
        print("COMPUTER WINS!")

        # Computer Takes the Human's Money
        human.bank_roll -= bet
        computer.bank_roll += bet
        print(f"Human Bank Roll: {human.bank_roll} & Computer Bank Roll: {computer.bank_roll}")
        break