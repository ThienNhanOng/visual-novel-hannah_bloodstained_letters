screen TicTacToeScreen():

    #Board background frame
    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        ysize 600
        background "#222"
        padding (0, 0, 0, 0)

        #3x3 tic-tac-toe grid - manual layout
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 10

            #Row 1
            hbox:
                xalign 0.5
                spacing 10

                #Cell 0
                button:
                    xysize (160, 160)
                    xalign 0.5
                    yalign 0.5
                    background "#888"
                    action Function(CellClicked, 0)

                #Cell 1
                button:
                    xysize (160, 160)
                    xalign 0.5
                    yalign 0.5
                    background "#888"
                    action Function(CellClicked, 1)

                #Cell 2
                button:
                    xysize (160, 160)
                    xalign 0.5
                    yalign 0.5
                    background "#888"
                    action Function(CellClicked, 2)

            #Row 2
            hbox:
                xalign 0.5
                spacing 10

                #Cell 3
                button:
                    xysize (160, 160)
                    xalign 0.5
                    yalign 0.5
                    background "#888"
                    action Function(CellClicked, 3)

                #Cell 4
                button:
                    xysize (160, 160)
                    xalign 0.5
                    yalign 0.5
                    background "#888"
                    action Function(CellClicked, 4)

                #Cell 5
                button:
                    xysize (160, 160)
                    xalign 0.5
                    yalign 0.5
                    background "#888"
                    action Function(CellClicked, 5)

            #Row 3
            hbox:
                xalign 0.5
                spacing 10

                #Cell 6
                button:
                    xysize (160, 160)
                    xalign 0.5
                    yalign 0.5
                    background "#888"
                    action Function(CellClicked, 6)

                #Cell 7
                button:
                    xysize (160, 160)
                    xalign 0.5
                    yalign 0.5
                    background "#888"
                    action Function(CellClicked, 7)

                #Cell 8
                button:
                    xysize (160, 160)
                    xalign 0.5
                    yalign 0.5
                    background "#888"
                    action Function(CellClicked, 8)

    #Show game-over panel if needed
    if TttState == TTTState.game_over:
        frame:
            xalign 0.5
            yalign 0.5
            background "#0008"
            padding (20, 20, 20, 20)
            vbox:
                xalign 0.5
                spacing 10
                text "Game Over!" size 36 color "#FFF" xalign 0.5
                textbutton "Return" action Return()



    #Calculate pieces position
    for i, cell in enumerate(TttBoard):
        if cell:
            $ row = i // 3
            $ col = i % 3
            $ x_pos = 0.4 + col * 0.1 #x positions for columns
            $ y_pos = [0.31, 0.5, 0.7][row] #y positions for rows
            text "[cell]" size 190 color "#FFF" xalign x_pos yalign y_pos

    #dev exit
    key "p" action Return()