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
else:
    exit(1) #OSX >>> Wip