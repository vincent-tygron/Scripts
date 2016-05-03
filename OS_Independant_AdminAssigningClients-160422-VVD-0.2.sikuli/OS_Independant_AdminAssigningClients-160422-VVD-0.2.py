import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Assigning clients to team...")

if Settings.isLinux() or Settings.isWindows():

    for x in range(0, 10):
        while exists("MainMenu-MultiPlayer-ClientBtn-160426-VVD-0.1.png", x):
            click()
            click("MainMenu-MultiPlayer-SettingsBtn-160426-VVD-0.1.png")
            click("MainMenu-MultiPlayer-ServerBtn-160426-VVD-0.1.png")
            #waitVanish("MainMenu-MultiPlayer-ClientBtn-160426-VVD-0.1.png")
            break

#########################################
# Check if all clients are connected... #
#########################################
    if exists("Admin-MultiPlayer-FourClientsConnected-160422-VVD-0.1.png", 30):
        print"[success] Clients were successfully invited and connected!"
        logging.info("[success] Clients were successfully invited and connected!")
    else:
        print"[error] Clients were not connected (in time)!"
        logging.error("[error] Clients were not connected (in time)!")
        exit(1)

else:
    exit(1) #OSX >>> Wip