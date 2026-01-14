#first visit tracking
default first_visit_shop = False

#placeholder test
label shoproom:
    scene bg room1
    
    if first_visit_shop == False:
        Sage "welcome to the Community Store!"
        Sage "my name is Sage. I also run the journalist club!"
    else:
        Sage "welcome back to the Community Store!"
    call screen Shopscreen


    jump schoolmap