screen say(who, what):

    drag:
        drag_name "say"
        yalign 1.0
        drag_handle (0, 0, 1.0, 30)

        xalign 0.5

        window id "window":
            # Ensure that the window is smaller than the screen.
            xmaximum 600

            has vbox

            if who:
                text who id "who"

            text what id "what"