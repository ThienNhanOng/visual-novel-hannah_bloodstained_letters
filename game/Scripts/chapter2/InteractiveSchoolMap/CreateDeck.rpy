init -100 python:
    import random

    SUITS = ["hearts", "diamonds", "clubs", "spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    #card values for blackjack
    def card_value(rank):
        """Get numeric value of a card rank."""
        if rank in ["J", "Q", "K"]:
            return 10
        elif rank == "A":
            return 11
        else:
            return int(rank)
    
    #used to shuffle other things beside cards.
    #shuffle using fisher yates. o(n)
    def fisherYates(deck):
        cardAmount = len(deck)
        #start from the last index down to 1 and decrement each time
        for lastIndex in range(cardAmount-1, 0, -1): #start stop step
            #j is randomize index from 0 to i
            randomindex = renpy.random.randint(0, lastIndex)
            # Swap i and j
            deck[lastIndex], deck[randomindex] = deck[randomindex], deck[lastIndex]
    
    #create deck and shuffle upon creation
    def createDeck():
        new_deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = {
                    "rank": rank,
                    "suit": suit,
                    "value": card_value(rank)
                }
                new_deck.append(card)
        
        fisherYates(new_deck)
        
        return new_deck