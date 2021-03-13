###########################################
##### NAME: Greg Nickel          ##########
##### Uniqname: gnickel          ##########
###########################################

import unittest
import random

# Cards Class (Start)
class Card:
    '''a standard playing card
    cards will have a suit and a rank
    Class Attributes
    ----------------
    suit_names: list
        the four suit names in order
        0:Diamonds, 1:Clubs, 2: Hearts, 3: Spades
    faces: dict
        maps face cards' rank name
        1:Ace, 11:Jack, 12:Queen,  13:King
    Instance Attributes
    -------------------
    suit: int
        the numerical index into the suit_names list
    suit_name: string
        the name of the card's suit
    rank: int
        the numerical rank of the card
    rank_name: string
        the name of the card's rank (e.g., "King" or "3")
    '''
    suit_names = ["Diamonds","Clubs","Hearts","Spades"]
    faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}


    def __init__(self, suit=0,rank=2):
        self.suit = suit
        self.suit_name = Card.suit_names[self.suit]

        self.rank = rank
        if self.rank in Card.faces:
            self.rank_name = Card.faces[self.rank]
        else:
            self.rank_name = str(self.rank)

    def __str__(self):
        return f"{self.rank_name} of {self.suit_name}"


class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self):

        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card) # appends in a sorted order

    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i)

    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = [] # forming an empty list
        for c in self.cards: # each card in self.cards (the initial list)
            card_strs.append(c.__str__()) # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs: # if the string representing this card is not in the list already
            self.cards.append(card) # append it to the list

    def sort_cards(self):
        '''returns the Deck to its original order

        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)

    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck

        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck
        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

    def deal(self,number_of_hands,hand_size):
        '''Given a number of hands and size of hands, will shuffle the cards and
        deal out hand_sizes of to the given number of hands.
        If -1 as selected as the hand size, all cards will be dealt out.

        Parameters
        -------------------
        number_of_hands: int
            The number of hands dealt
        hand_size: int
            the number of cards to deal (deals all cards if set to -1)
        Returns
        -------
        list
            List of Hand objects
        '''
        self.shuffle() # Shuffle
        #Creates a list of hand lengths
        if number_of_hands*hand_size > 52:
            print("All cards will be dealt out, hand sizes might be unequal")
            hand_size = -1 #Defensive programming
        if hand_size == -1:
            small_hand = 52//number_of_hands #The length of the smallest hand
            extra_cards = 52%number_of_hands
            list_of_hand_lengths = []
            for i in range(number_of_hands):
                list_of_hand_lengths.append(small_hand)
            for i in range(extra_cards): #Distributes extra cards (if any)
                list_of_hand_lengths[i] += 1
        else:
            list_of_hand_lengths = []
            for i in range(number_of_hands):
                list_of_hand_lengths.append(hand_size)
        #Creates a hand for each given hand length
        list_of_hands = []
        for x in list_of_hand_lengths:
            list_of_hands.append(Hand(self.deal_hand(x)))
        return list_of_hands


def print_hand(hand):
    '''prints a hand in a compact form
    Parameters
    -------------------
    hand: list
        list of Cards to print
    Returns
    -------
    none
    '''
    hand_str = '/ '
    for c in hand:
        s = c.suit_name[0]
        r = c.rank_name[0]
        hand_str += r + "of" + s + ' / '
    print(hand_str)

#Cards Class (End)

# create the Hand with an initial set of cards

class Hand:
    '''a hand for playing card
    Class Attributes
    ----------------
    None

    Instance Attributes
    -------------------
    init_card: list
        a list of cards
    '''
    def __init__(self, init_cards=[]):
        self.cards = init_cards

    def add_card(self, card):
        '''add a card
        add a card to the hand
        silently fails if the card is already in the hand
        Parameters
        -------------------
        card: instance
        a card to add
        Returns
        -------
        None
        '''
        self.cards.append(card)

    def remove_card(self, card):
        '''remove a card from the hand
        Parameters
        -------------------
        card: instance
        a card to remove
        Returns
        -------
        the card, or None if the card was not in the Hand
        '''
        if card in self.cards:
            index_number = self.cards.index(card)
            return self.cards.pop(index_number)
        else:
            return None

    def draw(self, deck):
        '''draw a card
        draw a card from a deck and add it to the hand
        side effect: the deck will be depleted by one card
        Parameters
        -------------------
        deck: instance
        a deck from which to draw
        Returns
        -------
        None
        '''
        new_card = deck.deal_card()
        self.cards.append(new_card)

    def remove_pairs(self):
        '''Search through a given hand and remove cards with the same rank
        Created a dictionary of lists to store card by ranks
        Sorts cards into each dictionary list
        Removes pairs or quadruples
        Clears hands
        ReAdd suriving cards in dictionary into the self.cards list

        Parameters
        -------------------
        None

        Returns
        -------
        None
        '''
        sorted = {}
        for i in range(13):
            sorted[i] = []
        for card in self.cards:
            sorted[card.rank].append(card)
        for key, val in sorted.items():
            if len(val) == 4:
                sorted[key] = []
            elif len(val) >= 2:
                sorted[key].pop()
                sorted[key].pop() #Magnitude4life #Six Seasons and movie
        self.cards.clear()
        for val in sorted.values():
            self.cards.extend(val)



