import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Assigning clients to team...")

if Settings.isLinux() or Settings.isWindows():

    for x in range(0, 10):
        while exists("MainMenu-MultiPlayer-ClientBtn-160426-VVD-0.1.png", x):
            click()
            click("Admin-CG5-LevelBtn-160428-VVD-0.1.png")
            click("MainMenu-MultiPlayer-SettingsBtn-160509-VVD-0.1.png")
            click("MainMenu-MultiPlayer-ServerBtn-160426-VVD-0.1.png")
            break

elif Settings.isMac():

    for x in range(0, 10):
        while exists(Pattern("1462882460519.png").exact(),x):
            click()
            click("1462882491645.png")
            click("1462882535453.png")
            click("1462882553117.png")
            break
    
else:
    print"[error] OS error!"
    logging.error("[error] OS error!")
    exit(1) 