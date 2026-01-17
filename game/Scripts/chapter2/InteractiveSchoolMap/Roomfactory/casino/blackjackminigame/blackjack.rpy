#Game state variables (persisted by Renpy)
default deck = []
default player_hand = []
default round_active = False
default current_bet = 0
#default CasinoMoney = 10000 #value will be override by global money
default CasinoMoney = 11
default dealer_total = 0
default game_over = False
#placeholder for win lose push
default message = ""
default result = ""

# Deck/rank definitions (constants, not mutable state)
init -100 python:
    import random

    #for face cards
    #dictionary to map face card names to image file names
    FACE_CARD_NAMES = {"A": "ace", "J": "jack", "Q": "queen", "K": "king"}
    
    def card_image_path(card):
        """Get the image path for a card."""
        rank = card["rank"]
        rank_name = FACE_CARD_NAMES.get(rank, rank)
        return "blackjack/{}_of_{}.png".format(rank_name, card["suit"])

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

    #Game control functions
    def start_game(bet=10):
        """Start a new blackjack round with the given bet amount."""
        if store.CasinoMoney < bet:
            return False
        
        store.CasinoMoney -= bet
        store.current_bet = bet
        store.deck = createDeck()
        store.player_hand = [store.deck.pop(), store.deck.pop()]
        store.round_active = True
        store.dealer_total = 0
        store.game_over = False
        
        hand_value = calculate_hand_value(store.player_hand)
        store.message = f"Player total: {hand_value}"
        renpy.restart_interaction()

    def hit_card():
        """Draw another card for the player."""
        if store.round_active == False or store.game_over:
            return
        
        if bool(store.deck) == False:
            store.deck = createDeck()
        
        store.player_hand.append(store.deck.pop())
        total = calculate_hand_value(store.player_hand)

        if total > 21:
            store.message = "BUST!"
            store.round_active = False
            store.game_over = True
        elif total == 21:
            store.message = "BLACKJACK!"
            store.CasinoMoney += store.current_bet * 2
            store.result = "win"
            store.round_active = False
            store.game_over = True
        else:
            store.message = f"Total: {total}"

    def stand_game():
        """End the round and determine the winner."""
        if store.game_over or store.round_active == False:
            return

        store.dealer_total = random.randint(16, 21)
        store.round_active = False
        player_total = calculate_hand_value(store.player_hand)

        if store.dealer_total > 21 or player_total > store.dealer_total:
            store.message = "You win!"
            store.CasinoMoney += store.current_bet * 2
            store.result = "win"
        elif player_total == store.dealer_total:
            store.message = "Push."
            store.CasinoMoney += store.current_bet
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
            store.CasinoMoney += store.current_bet
            store.current_bet = 0
        reset_round()
        renpy.restart_interaction()