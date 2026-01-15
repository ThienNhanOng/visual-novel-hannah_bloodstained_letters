screen blackjack_table():
    tag blackjack_table

    # Header (top-left): money, bet, dealer, and message
    frame:
        xalign 0.02
        yalign 0.02
        background None
        vbox:
            spacing 6
            text "Current Money: [playerMoney]" size 40 color "#f1de2e62"
            text "Bet: [current_bet]" size 50 color "#486e16"
            text "Dealer: [dealer_total]" size 50 color "#ff0000"
            if message:
                $ msgColor = "#ff0000" if message.startswith("Player total:") else "#ffffff"
                text message size 40 color msgColor

    # Deck placeholder (centered stack)
    frame:
        xalign 0.41
        yalign 0.485
        background None
        hbox:
            spacing 4
            add "blackjack/card_back.png" xysize (100, 170)
            add "blackjack/card_back.png" xysize (100, 170)
            add "blackjack/card_back.png" xysize (100, 170)
            add "blackjack/card_back.png" xysize (100, 170)

    # Extra hit cards (fixed positions)
    for i, pos in enumerate([0.5, 0.6, 0.7, 0.8, 0.9]):
        if len(player_hand) > 2 + i:
            add card_image_name(player_hand[2 + i]) xalign pos yalign 0.48 xysize (100, 170)

    # Player action buttons (top-center)
    frame:
        xalign 0.5
        yalign 0.18
        background None
        vbox:
            text "Player hand:" size 22
            hbox:
                spacing 10
                textbutton "Bet 10" action Function(start_game, 10) sensitive (not round_active and playerMoney >= 10)
                textbutton "Bet 50" action Function(start_game, 50) sensitive (not round_active and playerMoney >= 50)
                textbutton "Bet 100" action Function(start_game, 100) sensitive (not round_active and playerMoney >= 100)
                textbutton "All-IN" action Function(start_game, playerMoney) sensitive (not round_active and playerMoney > 0)
                textbutton "Hit" action Function(hit_card) sensitive round_active
                textbutton "Stand" action Function(stand_game) sensitive round_active
                textbutton "New Round" action Function(reset_round) sensitive game_over
                textbutton "Leave" action [Function(refund_and_leave), Return()] sensitive (not round_active)

    # Player hand display (bottom)
    if not player_hand:
        hbox:
            xalign 0.5
            yalign 0.9
            spacing 8
            add "blackjack/card_back.png" xysize (120, 190)
            add "blackjack/card_back.png" xysize (120, 190)
    else:
        hbox:
            xalign 0.5
            yalign 0.9
            spacing 8
            for card in player_hand[-10:]:
                add card_image_name(card) xysize (96, 144)

