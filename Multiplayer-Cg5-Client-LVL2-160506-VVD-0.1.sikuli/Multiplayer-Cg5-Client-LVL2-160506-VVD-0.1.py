import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

logging.info("[info] Play Level 2...")

if Settings.isLinux() or Settings.isWindows():

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

elif Settings.isMac():

    ################
    # Municipality #
    ################
    if exists():
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