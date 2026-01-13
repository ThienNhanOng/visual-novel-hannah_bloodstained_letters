default axescore = 0
default misclickcount = 0
# How often the target auto-moves Lower = faster.
default relocateintervalseconds = 1.8
# Target box size
default targetsizepixels = 140

# Where the slide starts
default startnormalizedx = 0.5
default startnormalizedy = 0.5
# Where the slide wants to end
default destinationnormalizedx = 0.5
default destinationnormalizedy = 0.5
# Slide progress from 0 (start) to 1 (done).
default slideprogress = 0.0
# Is the target currently moving?
default issliding = False
# The live normalized position used to render the target.
default targetnormalizedx = 0.5
default targetnormalizedy = 0.5

init python:
    import random, math

    def randomnormalizedcoordinate(margin):
        # Pick a 0..1 coordinate that keeps the target fully on-screen.
        return random.uniform(margin, 1.0 - margin)

    def respawntarget():
        # this allows a new destination and start sliding toward it.
        # Keeps the target inside the screen bounds.
        global startnormalizedx, startnormalizedy
        global destinationnormalizedx, destinationnormalizedy
        global slideprogress, issliding, slideduration
        global targetnormalizedx, targetnormalizedy, targetsizepixels

        sw = float(config.screenwidth)
        sh = float(config.screenheight)

        # Leave a little padding so the square never clips off-screen.
        marginx = max(0.0, (targetsizepixels / sw) * 0.5)
        marginy = max(0.0, (targetsizepixels / sh) * 0.5)

        # Start
        startnormalizedx = targetnormalizedx
        startnormalizedy = targetnormalizedy
        # Fresh destination inside the safe area.
        destinationnormalizedx = randomnormalizedcoordinate(marginx)
        destinationnormalizedy = randomnormalizedcoordinate(marginy)

        # Reset animation state.
        slideprogress = 0.0
        issliding = True

        # Time the slide by distance: short hops feel snappy, long ones don’t drag.
        dx = destinationnormalizedx - startnormalizedx
        dy = destinationnormalizedy - startnormalizedy
        dist = math.hypot(dx, dy)
        # Slow the slide so the axe drifts instead of snapping.
        slideduration = max(0.35, min(1.2, dist * 1.8))

    def updateslideanimation():
        # this uses the timer to simulate the frames update for x and y position
        # of an object
        global slideprogress, issliding
        global targetnormalizedx, targetnormalizedy
        global startnormalizedx, startnormalizedy
        global destinationnormalizedx, destinationnormalizedy, slideduration

        if not issliding:
            return

        # Called about every 0.05s by a timer.
        step = 0.05 / slideduration
        slideprogress = min(1.0, slideprogress + step)

        t = slideprogress
        t = t * t * (3.0 - 2.0 * t)

        targetnormalizedx = startnormalizedx + (destinationnormalizedx - startnormalizedx) * t
        targetnormalizedy = startnormalizedy + (destinationnormalizedy - startnormalizedy) * t

        if slideprogress >= 1.0:
            issliding = False
            targetnormalizedx = destinationnormalizedx
            targetnormalizedy = destinationnormalizedy

    def handletargethit():
        # Nice shot: +1 score, a bit faster, a bit smaller, then move again.
        global axescore, relocateintervalseconds, targetsizepixels
        axescore += 1
        # Play the hit bell; using renpy.sound in Python context.
        renpy.sound.play("audio/MusicAndSoundtracks/bell.wav", channel="sound")
        # Keep moves slower and tighten the decay so the axe lingers longer.
        relocateintervalseconds = max(2.0, relocateintervalseconds * 0.99)
        targetsizepixels = max(120, int(targetsizepixels * 0.95))
        respawntarget()

    def handlemissclick():
        # Clicked the background? Count a miss.
        global misclickcount
        misclickcount += 1

    def initializeclicker(axescore0=0, misclicks0=0, interval0=1.0, targetsize0=100):
        # Reset everything to clean defaults before the screen opens.
        global axescore, misclickcount, relocateintervalseconds, targetsizepixels
        global startnormalizedx, startnormalizedy
        global destinationnormalizedx, destinationnormalizedy
        global slideprogress, issliding
        global targetnormalizedx, targetnormalizedy

        axescore = axescore0
        misclickcount = misclicks0
        relocateintervalseconds = interval0
        targetsizepixels = targetsize0

        # Center the target.
        targetnormalizedx = 0.5
        targetnormalizedy = 0.5

        # Start and end both at the center.
        startnormalizedx = targetnormalizedx
        startnormalizedy = targetnormalizedy
        destinationnormalizedx = targetnormalizedx
        destinationnormalizedy = targetnormalizedy

        #initialize slide state with no movement.
        slideprogress = 0.0
        issliding = False

# Clicker mini-game screen.
screen clickerminigame():
    modal True

    # End the mini-game after 3 misses; show a quick summary and return the score.
    if misclickcount >= 3:
        add "images/chapter2/forestroompictures/need remove bg/axe.jpeg"
        frame:
            xalign 0.5
            yalign 0.4
            padding (20, 20)
            text "Game Over" size 60 xalign 0.5
            text "Score: [axescore]" size 40 xalign 0.5
        timer 0.1 action Return(axescore)
    else:
        # Backdrop
        add "bg black"

        # Tiny HUD for score, misses, and auto-move speed.
        frame:
            xalign 0.02
            yalign 0.02
            padding (12, 8)
            has hbox
            text "Score: [axescore]" size 26
            text "Miss clicked: [misclickcount]/3" size 26

        # Auto-move the target on a schedule.
        timer relocateintervalseconds repeat True action Function(respawntarget)
        # Drive the in-between motion (~20 FPS).
        timer 0.05 repeat True action Function(updateslideanimation)

        # Click anywhere that's not the target to record a miss.
        button:
            xfill True
            yfill True
            background None
            action Function(handlemissclick)

        # The target button: positioned by normalized coords, sized in pixels, optional sprite overlay.
        button:
            align (targetnormalizedx, targetnormalizedy)
            xsize targetsizepixels
            ysize targetsizepixels
            background None
            hover_background None
            if renpy.loadable("images/axenobg.png"):
                # Render only the axe sprite; button still captures clicks in its bounds.
                add im.Scale("images/axenobg.png", targetsizepixels, targetsizepixels)
            else:
                # Transparent fallback keeps the hitbox without showing a red box.
                add Solid("#0000")
            action Function(handletargethit)

# Wrapper label: call this to run the mini-game and get the final score back.
label clickergame:
    $ initializeclicker()
    call screen clickerminigame

    if axescore >= 5 and axescore <= 10:
        $ Miacounter += 1
    elif axescore >= 10:
        $ Theocounter += 1
    "Counter: mia | [Miacounter] | silas [Silascounter] | theo [Theocounter]|"
    return return
