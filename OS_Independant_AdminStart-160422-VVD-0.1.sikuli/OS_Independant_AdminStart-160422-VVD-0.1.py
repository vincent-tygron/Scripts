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

else:#if Settings.isMac()
    exit(1) #Temp exit... WIP