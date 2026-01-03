screen Shopscreen():
    tag shop
    modal True
    zorder 20

    add "images/map/townmap/bg room1.png"

    frame:
        xalign 0.0
        yalign 0.5
        xsize 0.5 * config.screen_width
        yfill True
        background "#0008"
        padding (24, 24)

        vbox:
            spacing 12

            hbox:
                spacing 18
                vbox:
                    spacing 6
                    button:
                        xysize (200, 50)
                        action Return()
                        text "Leave" style "quick_button_text" size 28 color "#3cd070" hover_color "#ff0000"
                    text "Money: [Global_Money]" style "gui_text" size 28 color "#3cd070"

            viewport:
                draggable True
                mousewheel True
                xfill True
                yfill True

                vbox:
                    spacing 12
                    null height 120
                    for item in ShopItem:
                        $ owned = purchased_items.get(item.name, False)
                        $ available = canbuy(item)
                        
                        # Determine button text and color based on state
                        if owned:
                            $ btn_text = "Purchased"
                            $ color = "#c0c0c0"  # Gray for purchased
                            $ btn_action = NullAction()
                        elif available:
                            $ btn_text = "Buy [item.label]"
                            $ color = "#3cd070"  # Green for available
                            $ btn_action = Function(buyitem, item)
                        else:
                            $ btn_text = "Locked"
                            $ color = "#d74343"  # Red for locked
                            $ btn_action = NullAction()
                        
                        $ item_name = item.label
                        $ item_price = item.price
                        $ item_desc = item.desc

                        frame:
                            background "#0000"
                            xfill True
                            padding (8, 8)

                            vbox:
                                spacing 8

                                vbox:
                                    spacing 4
                                    text "Price: $$ [item_price]" color color style "button_text" size 22
                                    text "Description: [item_desc]" color color style "gui_text" size 20
                                    if owned:
                                        text "(Already purchased)" color "#c0c0c0" style "gui_text"

                                textbutton btn_text:
                                    style "choice_button"
                                    text_style "choice_button_text"
                                    text_color color
                                    action btn_action