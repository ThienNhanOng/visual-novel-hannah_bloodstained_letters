screen blackjack_table():
    tag blackjack_table

    # Header (top-left): money, bet, dealer, and message
    frame:
        xalign 0.02
        yalign 0.02
        background None
        vbox:
            spacing 6
            text "Current Money: [player_money]" size 40 color "#f1de2e62"
            text "Bet: [current_bet]" size 50 color "#486e16"
            text "Dealer: [dealer_total]" size 50 color "#ff0000"
            if message:
                $ msg_color = "#ff0000" if message.startswith("Player total:") else "#ffffff"
                text message size 40 color msg_color

    # Deck placeholder (centered stack)
    frame:
        xalign 0.41
        yalign 0.485
        background None
        hbox:
            spacing 4
            add "blackjack/card_back.png" xysize (120, 180)
            add "blackjack/card_back.png" xysize (120, 180)
            add "blackjack/card_back.png" xysize (120, 180)
            add "blackjack/card_back.png" xysize (120, 180)

    # Extra hit cards (fixed positions)
    for i, pos in enumerate([0.5, 0.6, 0.7, 0.8, 0.9]):
        if len(player_hand) > 2 + i:
            add card_image_path(player_hand[2 + i]) xalign pos yalign 0.48 xysize (120, 180)

    # Player action buttons (top-center)
    frame:
        xalign 0.5
        yalign 0.08
        background None
        vbox:
            text "Player hand:" size 22
            vbox:
                spacing 5
                xalign 0.5
                hbox:
                    spacing 15
                    textbutton "Bet 10" action Function(start_game, 10) sensitive (not round_active and player_money >= 10) text_size 56 background "#b0b0b0"
                    textbutton "Bet 50" action Function(start_game, 50) sensitive (not round_active and player_money >= 50) text_size 56 background "#b0b0b0"
                    textbutton "Bet 100" action Function(start_game, 100) sensitive (not round_active and player_money >= 100) text_size 56 background "#b0b0b0"
                    textbutton "All-IN" action Function(start_game, player_money) sensitive (not round_active and player_money > 0) text_size 56 background "#b0b0b0"
                hbox:
                    spacing 15
                    textbutton "Hit" action Function(hit_card) sensitive round_active text_size 56 background "#b0b0b0"
                    textbutton "Stand" action Function(stand_game) sensitive round_active text_size 56 background "#b0b0b0"
                    textbutton "New Round" action Function(reset_round) sensitive game_over text_size 56 background "#b0b0b0"
                    textbutton "Leave" action [Function(refund_and_leave), Return()] sensitive (not round_active) text_size 56 background "#b0b0b0"

    # Player hand display (bottom)
    if not player_hand:
        hbox:
            xalign 0.5
            yalign 0.9
            spacing 15
            add "blackjack/card_back.png" xysize (130, 200)
            add "blackjack/card_back.png" xysize (130, 200)
    else:
        hbox:
            xalign 0.5
            yalign 0.9
            spacing 15
            for card in player_hand[-10:]:
                add card_image_path(card) xysize (120, 180)

