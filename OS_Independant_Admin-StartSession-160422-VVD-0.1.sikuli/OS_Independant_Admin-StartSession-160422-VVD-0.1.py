import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Admin starts session...")

if Settings.isLinux() or Settings.isWindows():
#########################################
# Check if all clients are connected... #
#########################################
    if exists("Admin-MultiPlayer-FourClientsConnected-160422-VVD-0.1.png", 30):#Add 30 seconds if needed
        print"[success] Clients were successfully invited and connected!"
        logging.info("[success] Clients were successfully invited and connected!")
    else:
        print"[error] Clients were not connected (in time)!"
        logging.error("[error] Clients were not connected (in time)!")
        exit(1)
        
    click("Admin-MultiPlayer-SettingsBtn-160422-VVD-0.1.png")
    click("Admin-MultiPlayer-Settings-StartSessionBtn-160422-VVD-0.2.png")
    
    if exists("Admin-MultiPlayer-Settings-SessionsAreRunning-160422-VVD-0.1.png", 30):
        print"[success] Session has started!"
        logging.info("[success] Session has started!")
    else:
        print"[error] Session did not start in time and/ or as expected!"
        logging.error("[error] Session did not start in time and/ or as expected!")
        exit(1)

elif Settings.isMac():
#########################################
# Check if all clients are connected... #
#########################################
    #if exists("Admin-MultiPlayer-MAC-FourClientsConnected-160422-VVD-0.1.png", 30):#Add 30 seconds if needed
    if exists("1462882938643.png", 30):
        print"[success] Clients were successfully invited and connected!"
        logging.info("[success] Clients were successfully invited and connected!")
    else:
        print"[error] Clients were not connected (in time)!"
        logging.error("[error] Clients were not connected (in time)!")
        exit(1)
        
    #click("Admin-MultiPlayer-MAC-SettingsBtn-160422-VVD-0.1.png")
    click("1462882978082.png")
    #click("Admin-MultiPlayer-MAC-Settings-StartSessionBtn-160422-VVD-0.2.png")
    click("1462883004489.png")
    
    if exists("Admin-MultiPlayer-MAC-Settings-SessionsAreRunning-160422-VVD-0.1.png", 30):
        print"[success] Session has started!"
        logging.info("[success] Session has started!")
    else:
        print"[error] Session did not start in time and/ or as expected!"
        logging.error("[error] Session did not start in time and/ or as expected!")
        exit(1)

else:
    print"[error] OS error!"
    logging.error("[error] OS error!")
    exit(1)