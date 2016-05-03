import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Admin starts session...")

if Settings.isLinux() or Settings.isWindows():
    wait("Admin-MultiPlayer-SettingsBtn-160422-VVD-0.1.png")
    click()
    wait("Admin-MultiPlayer-Settings-StartSessionBtn-160422-VVD-0.2.png")
    click()
    if exists("Admin-MultiPlayer-Settings-SessionsAreRunning-160422-VVD-0.1.png", 30):
        print"[success] Session has started!"
        logging.info("[success] Session has started!")
    else:
        print"[error] Session did not start in time and/ or as expected!"
        logging.error("[error] Session did not start in time and/ or as expected!")
        exit(1)