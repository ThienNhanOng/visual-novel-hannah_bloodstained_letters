#first visit tracking
default first_visit_shop = False

#placeholder test
label shoproom:
    show sandyShop

    if first_visit_shop == False:
        Sage "welcome to the Community Store!"
        Sage "my name is Sage. I also run the journalist club!"
        $ first_visit_shop = True
    else:
        Sage "oh hey! welcome back to the Community Store!"
    call screen Shopscreen


    jump schoolmap