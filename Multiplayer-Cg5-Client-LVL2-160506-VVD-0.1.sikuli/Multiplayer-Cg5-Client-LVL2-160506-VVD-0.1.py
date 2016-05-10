import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

logging.info("[info] Play Level 2...")

if Settings.isLinux() or Settings.isWindows():

    if exists("Multiplayer-CG5-IntroPane-CntBtnl-160506-VVD-0.1.png"):
        print"[info] Level 2 has started..."
        logging.info("[info] Level 2 has started...")

    ################
    # Municipality #
    ################

    if exists(Pattern("Multiplayer-CG5-Municipality-LVL2-IntroPanel-160506-VVD-0.1.png").similar(0.80), 0):
        print"[info] Municipality switched to Level 2..." 
        logging.info("[info] Municipality switched to Level 2...")
        
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)

    ##############
    # Waterboard #
    ##############
    elif exists("Multiplayer-CG5-Waterboard-LVL2-IntroPanel-160506-VVD-0.1.png", 0):
        print"[info] Waterboard switched to Level 2..." 
        logging.info("[info] Waterboard switched to Level 2...")
        
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
       
    #######
    # SSH #
    #######
    elif exists("Multiplayer-CG5-SSH-LVL2-IntroPanel-160506-VVD-0.1.png", 0):
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

    if exists("Multiplayer-CG5-MAC-IntroPane-CntBtnl-160506-VVD-0.1.png"):
        print"[info] Level 2 has started..."
        logging.info("[info] Level 2 has started...")

    ################
    # Municipality #
    ################
    if exists(Pattern("Multiplayer-CG5-MAC-Municipality-LVL2-IntroPanel-160506-VVD-0.1.png").similar(0.90), 0):
        print"[info] Municipality switched to Level 2..."
        logging.info("[info] Municipality switched to Level 2...")

        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
    ##############
    # Waterboard #
    ##############
    elif exists("Multiplayer-CG5-MAC-Waterboard-LVL2-IntroPanel-160510-VVD-0.1.png", 0):
        print"[info] Waterboard switched to Level 2..." 
        logging.info("[info] Waterboard switched to Level 2...")
        
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
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