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
        click("Admin-CG5-TopBar-Messages-Sender-160428-VVD-0.1.png")
        wait("Admin-CG5-TopBar-Messages-ReplyBtn-160428-VVD-0.1.png")
        click()
        #wait("Admin-CG5-TopBar-Messages-ReplyBtn-160428-VVD-0.1.png")
        #click()
        click("Admin-CG5-GlobalBtn-160428-VVD-0.1.png")

elif Settings.isMac():

    if exists("1462884531540.png", 60):
        click("1462884545549.png")
        wait("1462884568365.png")
        click()
        wait("1462884601787.png")
        click()
        wait("1462884624587.png")
        click()
        #wait("Admin-CG5-TopBar-Messages-ReplyBtn-160428-VVD-0.1.png")
        #click()
        click("1462884638290.png")


else:
    print"WIP - OS error"
    exit(1)