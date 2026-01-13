#Game state variables (persisted by Ren'Py)
default deck = []
default player_hand = []
default round_active = False
default current_bet = 0
#default playerMoney = 10000 #debug starting money
default playerMoney = 11
default dealer_total = 0
default game_over = False
#placeholder for win lose push
default message = ""


init -100 python:
    import random

    global deck, player_hand, round_active, current_bet, playerMoney, dealer_total, game_over, message

    #Deck/rank definitions
    suits = ["hearts", "diamonds", "clubs", "spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def card_value(rank):
        if rank in ["J", "Q", "K"]:
            return 10
        elif rank == "A":
            return 11
        #fixes issue with renpy treating int as str
        else:
            return int(rank)

    #Create a new list of cards for the deck and shuffle
    def makeNewDeck():
        newDeck = [] #initialize empty list to hold deck
        for oneSuit in suits:
            # Go through every rank
            for rank in ranks:
                # Make one card (a dictionary)
                oneCard = {}
                oneCard["rank"] = rank
                oneCard["suit"] = oneSuit
                oneCard["value"] = card_value(rank)

                # Add the card to the deck
                newDeck.append(oneCard)

        # Mix the cards so order is random
        renpy.random.shuffle(newDeck)

        return newDeck

    #creates a hand
    def create_hand(hand):
        handValue = 0
        aces = 0
        #sum
        for card in hand:
            #Using a dictionary to map every card to its value
            handValue = handValue + card["value"]
            #Account for aces in case we go over 21
            if card["rank"] == "A":
                aces = aces + 1
        
        # Adjust for aces if we're over 21
        while handValue > 21 and aces > 0:
            handValue = handValue - 10
            aces = aces - 1
        return handValue


    #for face cards
    #dictionary to map face card names to image file names
    faceCardNames = {"A": "ace", "J": "jack", "Q": "queen", "K": "king"}
    def card_image_name(card):
        rank = card["rank"]
        rank_name = faceCardNames.get(rank, rank)
        return "blackjack/{}_of_{}.png".format(rank_name, card["suit"]) 


    #Game control functions (without renpy.notify)
    def start_game(bet=10): #fallback because minimum bet is 10
        #notify renpy that global variables exists.
        #variables were defined at init level .
        global deck, player_hand, round_active, current_bet, playerMoney, dealer_total, game_over, message
        
        
        if playerMoney < bet:
            return False
        current_bet = bet
        playerMoney -= bet

        #reset deck and hands
        deck = makeNewDeck()
        player_hand = [deck.pop(), deck.pop()]
        round_active = True
        dealer_total = 0

        #Clear any previous round state here so renpy language shows the new round
        game_over = False
        
        #Override and display hand total
        message = f"Player total: {create_hand(player_hand)}"
        renpy.restart_interaction()

    def hit_card():
        global deck, player_hand, round_active, game_over, message
        if not round_active or game_over: #check to make sure not currently playing
            return
        if not deck:
            deck = makeNewDeck() #to make a new deck
        player_hand.append(deck.pop()) #remove the cards drawn from deck
        total = create_hand(player_hand) #calculate total value of hand

        #game condition
        if total > 21:
            message = "BUST!"
            round_active = False
            game_over = True
        elif total == 21:
            message = "BLACKJACK!"
            round_active = False
            game_over = True
        else:
            message = "Total: " + str(total)

    #resolve round and display results
    def stand_game():
        global round_active, dealer_total, playerMoney, current_bet, game_over, message
        if game_over or not round_active:
            return

        dealer_total = random.randint(17, 21)
        round_active = False
        player_total = create_hand(player_hand)

        #Game logic
        if dealer_total > 21 or player_total > dealer_total:
            message = "You win!"
            playerMoney += current_bet * 2
        elif player_total == dealer_total:
            message = "Push."
            playerMoney += current_bet
        else:
            message = "Dealer wins."

        current_bet = 0
        game_over = True
        renpy.restart_interaction()

    #reset interaction using renpy function
    def reset_round():
        """Reset the round state so the player can place a new bet."""
        global player_hand, round_active, current_bet, game_over, message, dealer_total
        player_hand = []
        round_active = False
        current_bet = 0
        game_over = False
        message = ""
        dealer_total = 0
        renpy.restart_interaction()

    #Refund the current bet and reset round state.
    def refund_and_leave():
        
        global playerMoney, current_bet
        if current_bet > 0:
            playerMoney += current_bet
            current_bet = 0
        reset_round()
        renpy.restart_interaction()