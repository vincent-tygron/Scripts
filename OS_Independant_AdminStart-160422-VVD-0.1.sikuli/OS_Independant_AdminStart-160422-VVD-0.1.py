import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Starting Admin Application for Cg5 session...")

##########################
# First start 4 clients! #
##########################

if Settings.isLinux() or Settings.isWindows():
    wait("MainMenu-MultiPlayerBtn-160422-VVD-0.1.png", 3)
    click()
    wait("MainMenu-MultiPlayer-StartNewSessionBtn-160422-VVD-0.1.png", 3)
    click()
    wait("MainMenu-MultiPlayer-SearchProjectsField-160422-VVD-0.1.png", 3)
    click()
    paste("cg5")
    type(Key.ENTER)
    wait("MainMenu-MultiPlayer-Cg5Btn-160422-VVD-0.1.png", 3)
    click()
    wait("MainMenu-MultiPlayer-StartSingleSessionBtn-160422-VVD-0.1.png", 3)
    click()
    if exists("MainMenu-MultiPlayer-Admin-Team1Btn-160422-VVD-0.1.png", 900):
        print"[success] Cg5 session ready!"
        logging.info("[success] Cg5 session ready!")

elif Settings.isMac():

    wait("1462882029995.png", 3)
    click()
    wait("1462882086368.png",3)
    click()
    wait("1462882116663.png",3)
    click()
    paste("cg5")
    type(Key.ENTER)
    wait("1462882151614.png",3)
    click()
    wait("1462882194613.png",3)
    click()
    if exists("1462882239612.png",900):
        print"[success] Cg5 session ready!"
        logging.info("[success] Cg5 session ready!")

else:
    print"[error] OS error!"
    logging.error("[error] OS error!")
    exit(1)
