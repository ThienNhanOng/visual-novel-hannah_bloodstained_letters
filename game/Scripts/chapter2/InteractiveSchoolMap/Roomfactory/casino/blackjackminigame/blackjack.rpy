#Game state variables (persisted by Ren'Py)
default deck = []
default player_hand = []
default round_active = False
default current_bet = 0
#default player_money = 10000 #debug starting money
default player_money = 11
default dealer_total = 0
default game_over = False
#placeholder for win lose push
default message = ""
default result = ""

# Deck/rank definitions (constants, not mutable state)
init -100 python:
    import random

    SUITS = ["hearts", "diamonds", "clubs", "spades"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def card_value(rank):
        """Get numeric value of a card rank."""
        if rank in ["J", "Q", "K"]:
            return 10
        elif rank == "A":
            return 11
        else:
            return int(rank)

    #Create a new list of cards for the deck and shuffle
    def make_new_deck():
        """Create and shuffle a new deck of cards."""
        new_deck = []
        for suit in SUITS:
            for rank in RANKS:
                card = {
                    "rank": rank,
                    "suit": suit,
                    "value": card_value(rank)
                }
                new_deck.append(card)
        
        renpy.random.shuffle(new_deck)
        return new_deck

    def calculate_hand_value(hand):
        """Calculate the total value of a hand, adjusting for aces."""
        hand_value = 0
        aces = 0
        
        for card in hand:
            hand_value += card["value"]
            if card["rank"] == "A":
                aces += 1
        
        # Adjust for aces if we're over 21
        while hand_value > 21 and aces > 0:
            hand_value -= 10
            aces -= 1
        
        return hand_value


    #for face cards
    #dictionary to map face card names to image file names
    FACE_CARD_NAMES = {"A": "ace", "J": "jack", "Q": "queen", "K": "king"}
    
    def card_image_path(card):
        """Get the image path for a card."""
        rank = card["rank"]
        rank_name = FACE_CARD_NAMES.get(rank, rank)
        return "blackjack/{}_of_{}.png".format(rank_name, card["suit"]) 


    #Game control functions
    def start_game(bet=10):
        """Start a new blackjack round with the given bet amount."""
        if store.player_money < bet:
            return False
        
        store.player_money -= bet
        store.current_bet = bet
        store.deck = make_new_deck()
        store.player_hand = [store.deck.pop(), store.deck.pop()]
        store.round_active = True
        store.dealer_total = 0
        store.game_over = False
        
        hand_value = calculate_hand_value(store.player_hand)
        store.message = f"Player total: {hand_value}"
        renpy.restart_interaction()

    def hit_card():
        """Draw another card for the player."""
        if not store.round_active or store.game_over:
            return
        
        if not store.deck:
            store.deck = make_new_deck()
        
        store.player_hand.append(store.deck.pop())
        total = calculate_hand_value(store.player_hand)

        if total > 21:
            store.message = "BUST!"
            store.round_active = False
            store.game_over = True
        elif total == 21:
            store.message = "BLACKJACK!"
            store.round_active = False
            store.game_over = True
        else:
            store.message = f"Total: {total}"

    def stand_game():
        """End the round and determine the winner."""
        if store.game_over or not store.round_active:
            return

        store.dealer_total = random.randint(3, 4)
        store.round_active = False
        player_total = calculate_hand_value(store.player_hand)

        if store.dealer_total > 21 or player_total > store.dealer_total:
            store.message = "You win!"
            store.player_money += store.current_bet * 2
            store.result = "win"
        elif player_total == store.dealer_total:
            store.message = "Push."
            store.player_money += store.current_bet
            store.result = "push"
        else:
            store.message = "Dealer wins."
            store.result = "lose"

        store.current_bet = 0
        store.game_over = True
        renpy.restart_interaction()

    def reset_round():
        """Reset the round state so the player can place a new bet."""
        store.player_hand = []
        store.round_active = False
        store.current_bet = 0
        store.game_over = False
        store.message = ""
        store.dealer_total = 0
        renpy.restart_interaction()

    def refund_and_leave():
        """Refund the current bet and reset the round state."""
        if store.current_bet > 0:
            store.player_money += store.current_bet
            store.current_bet = 0
        reset_round()
        renpy.restart_interaction()