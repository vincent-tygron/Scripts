import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Admin runs session LVL1...")

if Settings.isLinux() or Settings.isWindows():
    if exists("Admin-CG5-Team1-MessageIcon2-160428-VVD-0.1.png", 60):
        click("Admin-CG5-Team1-MessageIcon-160428-VVD-0.1.png")
        wait("Admin-CG5-TopBar-MessageIcon-160428-VVD-0.1.png")
        click()
        wait("Admin-CG5-TopBar-Messages-Sender-160428-VVD-0.1.png")
        click()
        wait("Admin-CG5-TopBar-Messages-ReplyBtn-160428-VVD-0.1.png")
        click()
        #wait("Admin-CG5-TopBar-Messages-ReplyBtn-160428-VVD-0.1.png")
        #click()
        click("Admin-CG5-GlobalBtn-160428-VVD-0.1.png")

elif Settings.isMac():
    print"WIP - MAC not scripted yet!"
    exit(1)

else:
    print"WIP - OS error"
    exit(1)