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
    #######
    # SSH #
    #######
    if exists("Multiplayer-CG5-SSH-LVL2-IntroPanel-160506-VVD-0.1.png"):
        print"[info] SSH switched to Level 2..." 
        logging.info("[info] SSH switched to Level 2...")
        
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
                
    ###################
    # UNI Real Estate #
    ###################

    else:
        print"[info] Uni Real Estate switched to Level2..." 
        logging.info("[info] Uni Real Estate switched to Level2...")
        
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
        
elif Settings.isMac():

    ################
    # Municipality #
    ################
    if exists("Multiplayer-CG5-MAC-Municipality-LVL2-IntroPanel-160506-VVD-0.1.png"):
        print"[info] Switched to Level 2..."
        logging.info("[info] Switched to Level 2...")

        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
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