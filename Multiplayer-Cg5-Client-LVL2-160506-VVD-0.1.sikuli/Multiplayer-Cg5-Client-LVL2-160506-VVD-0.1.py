import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

logging.info("[info] Play Level 2...")

if Settings.isLinux() or Settings.isWindows():

    ################
    # Municipality #
    ################

#WIP - See Mac

    ##############
    # Waterboard #
    ##############
    if exists("Multiplayer-CG5-Waterboard-LVL2-IntroPanel-160506-VVD-0.1.png"):
        print"[info] Waterboard switched to Level 2..." 
        logging.info("[info] Waterboard switched to Level 2...")
        
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)

    else:
        exit(1)
'''        
        wait(, 3)
        doubleClick()
        wait(, 3)
        
    #######
    # SSH #
    #######

    ###################
    # UNI Real Estate #
    ###################

elif Settings.isMac():

    ################
    # Municipality #
    ################

    ##############
    # Waterboard #
    ##############

    #######
    # SSH #
    #######

    ###################
    # UNI Real Estate #
    ###################

else:
    print"[error] OS error!"
    logging.error("[error] OS error!")
    exit(1)
'''