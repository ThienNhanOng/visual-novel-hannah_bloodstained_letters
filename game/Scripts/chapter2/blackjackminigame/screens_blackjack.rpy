screen blackjack_table():
    tag blackjack_table
    #Fixed. screen is static and does not change when introducing new elements.
    fixed:
        #Placeholder labels top left (made red)
        text "Current Money: [player_money]" xalign 0.02 yalign 0.02 size 40 color "#f1de2e62"
        text "Bet: [current_bet]" xalign 0.28 yalign 0.02 size 50 color "#486e16"
        # Show the dealer's current total in the top-left area.
        text "Dealer: [dealer_total]" xalign 0.03 yalign 0.55 size 50 color "#ff0000"
        if message:
            # Move the message down so it doesn't overlap the dealer text.
            # If this is the player total message, make it red. Otherwise use default color.
            if message.startswith("Player total:"):
                text message xalign 0.02 yalign 0.4 size 40 color "#ff0000"
            else:
                text message xalign 0.02 yalign 0.4 size 40

        #just a deck placeholder image
        add "blackjack/card_back.png" xalign 0.4 yalign 0.485 xysize (100, 170)
        add "blackjack/card_back.png" xalign 0.405 yalign 0.485 xysize (100, 170)
        add "blackjack/card_back.png" xalign 0.410 yalign 0.485 xysize (100, 170)
        add "blackjack/card_back.png" xalign 0.415 yalign 0.485 xysize (100, 170)

        #set positions for hit cards at a fixed x positions
        for i, pos in enumerate([0.5, 0.6, 0.7, 0.8, 0.9]):
            if len(player_hand) > 2 + i:
                #set the hit cards images
                add card_image_name(player_hand[2 + i]) xalign pos yalign 0.48 xysize (100, 170)

    # when player hands are empty show starting hand positions
        # Player action buttons (near the top-center)
        frame xalign 0.5 yalign 0.18:
            vbox:
                text "Player hand:" size 22
                hbox:
                    spacing 10
                    textbutton "Bet 10" action Function(start_game, 10) sensitive (not round_active and player_money >= 10)
                    textbutton "Bet 50" action Function(start_game, 50) sensitive (not round_active and player_money >= 50)
                    textbutton "Bet 100" action Function(start_game, 100) sensitive (not round_active and player_money >= 100)
                    textbutton "All-IN" action Function(start_game, player_money) sensitive (not round_active and player_money > 0)
                    textbutton "Hit" action Function(hit_card) sensitive round_active
                    textbutton "Stand" action Function(stand_game) sensitive round_active
                    textbutton "Leave" action [Function(refund_and_leave), Return()]
                    # When a round ends (game_over True), offer a button to
                    # reset the round so the player can place a new bet.
                    textbutton "New Round" action Function(reset_round) sensitive game_over

        if not player_hand:
            add "blackjack/card_back.png" xalign 0.45 yalign 0.9 xysize (120, 190)
            add "blackjack/card_back.png" xalign 0.55 yalign 0.9 xysize (120, 190)

        hbox xalign 0.5 yalign 0.9:
            spacing 8
            for card in player_hand[-10:]:
                # Add the image directly to fixed x position for hand cards
                add card_image_name(card) xysize (96, 144)

