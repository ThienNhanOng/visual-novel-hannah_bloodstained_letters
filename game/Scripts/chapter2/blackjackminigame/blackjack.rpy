# Game state variables (persisted by Ren'Py)
default deck = []
default player_hand = []
default round_active = False
default current_bet = 0
#default playerMoney = 10000 #debug starting money
default playerMoney = 11
default dealer_total = 0
default game_over = False
default message = ""
default result = "" #default result


init -100 python:
    import random
    # Deck/rank definitions
    suits = ["hearts", "diamonds", "clubs", "spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def card_value(rank):
        if rank in ["J", "Q", "K"]:
            return 10
        elif rank == "A":
            return 11
        else:
            return int(rank)

    # Deck creation
    def create_deck():
        deck = [{"rank": r, "suit": s, "value": card_value(r)} for s in suits for r in ranks]
        random.shuffle(deck)
        return deck

    # Hand evaluation
    def create_hand(hand):
        total = sum(card["value"] for card in hand)
        aces = sum(1 for card in hand if card["rank"] == "A")
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    # Image helper
    royal_card_names = {"A": "ace", "J": "jack", "Q": "queen", "K": "king"}

    def card_image_name(card):
        rank = card["rank"]
        rank_name = royal_card_names.get(rank, rank)
        return "blackjack/{}_of_{}.png".format(rank_name, card["suit"]) 


    # Game control functions (without renpy.notify)
    def start_game(bet=10):
        # Include game_over and message in globals so we correctly reset them
        global deck, player_hand, round_active, current_bet, playerMoney, dealer_total, game_over, message
        if playerMoney < bet:
            return False
        current_bet = bet
        playerMoney -= bet
        deck = create_deck()
        player_hand = [deck.pop(), deck.pop()]
        round_active = True
        dealer_total = 0
        # Clear any previous round state here so UI shows the new round
        game_over = False
        # Show the player's starting hand total in the message area
        message = f"Player total: {create_hand(player_hand)}"
        return

    def player_hit():
        global deck, player_hand, round_active
        if not round_active:
            return
        if not deck:
            deck = create_deck()
        player_hand.append(deck.pop())
        if create_hand(player_hand) > 21:
            round_active = False
            return "bust"
        return "ok"

    def player_stand():
        global round_active, dealer_total
        if not round_active:
            return
        dealer_total = random.randint(17, 21)
        round_active = False
        return resolve_round()

    def resolve_round():
        global playerMoney, current_bet
        p = create_hand(player_hand)
        d = dealer_total
        # Log state before payout for debugging
        try:
            renpy.log(f"resolve_round BEFORE: p={p}, d={d}, current_bet={current_bet}, playerMoney={playerMoney}")
        except Exception:
            pass
        if d > 21 or p > d:
            playerMoney += current_bet * 2
            result = "win"
        elif p == d:
            playerMoney += current_bet
            result = "push"
        else:
            result = "lose"
        # Log state after payout
        try:
            renpy.log(f"resolve_round AFTER: result={result}, playerMoney={playerMoney}")
        except Exception:
            pass
        current_bet = 0
        # Ensure UI updates immediately to reflect the changed money/counts
        try:
            renpy.restart_interaction()
        except Exception:
            pass
        return result

    def hit_card():
        global deck, player_hand, round_active, game_over, message
        if not round_active or game_over: #check to make sure not currently playing
            return
        if not deck:
            deck = create_deck() #to make a new deck
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

    def stand_game():
        global round_active, dealer_total, playerMoney, current_bet, game_over, message
        
        if game_over or not round_active:
            return

        dealer_total = random.randint(17, 21)
        round_active = False
        p = create_hand(player_hand)
        d = dealer_total

        # Safe renpy.log call
        if hasattr(renpy, "log"):
            renpy.log(f"stand_game BEFORE: p={p}, d={d}, current_bet={current_bet}, playerMoney={playerMoney}")

        # Game logic
        if d > 21 or p > d:
            message = "You win!"
            playerMoney += current_bet * 2
        elif p == d:
            message = "Push."
            playerMoney += current_bet
        else:
            message = "Dealer wins."

        # Safe renpy.log
        if hasattr(renpy, "log"):
            renpy.log(f"stand_game AFTER: message={message}, playerMoney={playerMoney}")

        current_bet = 0
        game_over = True

        # Safe interaction refresh
        if hasattr(renpy, "restart_interaction"):
            renpy.restart_interaction()

    def reset_round():
        """Reset the round state so the player can place a new bet.

        This does NOT modify `playerMoney` — wins/loses already updated
        by `stand_game` / `resolve_round` / `hit_card`.
        """
        global deck, player_hand, round_active, current_bet, game_over, message, dealer_total
        # Keep deck as-is (so remaining cards carry forward), but clear
        # the player's hand and round flags so they can bet again.
        player_hand = []
        round_active = False
        current_bet = 0
        game_over = False
        message = ""
        dealer_total = 0
        # Refresh UI after resetting the round
        try:
            renpy.restart_interaction()
        except Exception:
            pass

    def refund_and_leave():
        #Refund the current bet (if any) and reset round state.
        global playerMoney, current_bet
        try:
            if current_bet and current_bet > 0:
                playerMoney += current_bet
                current_bet = 0
        except Exception:
            pass
        # Reset UI/round state so the table clears cleanly
        try:
            reset_round()
        except Exception:
            pass
        try:
            renpy.restart_interaction()
        except Exception:
            pass

    