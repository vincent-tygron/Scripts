import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

logging.info("[info] Accept invite and load Cg5 session...")

if Settings.isLinux() or Settings.isWindows():
    wait("Multiplayer-Client-InviteMessage-160422-VVD-0.1.png", FOREVER)
    click("Multiplayer-Client-InviteMessage-YesBtn-160422-VVD-0.1.png")
    if exists("Multiplayer-Client-Cg5-SplashScreen-160422-VVD-0.1.png", 60):
        print"[success] Client is connected to session!"
        logging.info("[success] Client is connected to session!")
    else:
        print"[error] Client did not connect to session (in time)!"
        logging.error("[error] Client did not connect to session (in time)!")
        exit(1)

if Settings.isMac():
    wait("Multiplayer-Client-MAC-InviteMessage-160425-VVD-0.1.png", FOREVER)
    click("Multiplayer-Client-MAC-InviteMessage-YesBtn-160422-VVD-0.1.png")
    if exists("Multiplayer-Client-MAC-Cg5-SplashScreen-160422-VVD-0.1.png", 60):
        print"[success] Client is connected to session!"
        logging.info("[success] Client is connected to session!")
    else:
        print"[error] Client did not connect to session (in time)!"
        logging.error("[error] Client did not connect to session (in time)!")
        exit(1)    