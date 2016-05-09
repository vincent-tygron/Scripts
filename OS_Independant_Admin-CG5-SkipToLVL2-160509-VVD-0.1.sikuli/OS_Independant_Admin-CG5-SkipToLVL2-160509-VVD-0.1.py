import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Admin waits for results and skips to LVL2...")

if Settings.isLinux() or Settings.isWindows():
    
    wait("Admin-CG5-Settings-SpeedUpBtn-160429-VVD-0.1.png")
    click()
    click()
    click()
    #wait(30)
    
    click("Admin-CG5-Team1-TeamIcon-160428-VVD-0.1.png")
    click("Admin-CG5-Team1-StatusBtn-160428-VVD-0.1.png")
    #if exists(Pattern("Admin-CG5-Team1-ResultsScore-160428-VVD-0.1.png").exact(), 300):
    #if exists(Pattern("Admin-CG5-Team1-LVL1-TeamScore-160509-VVD-0.1.png").exact(), 300):
    if exists(Pattern("Admin-CG5-Team1-LVL1-TeamScore-160509-VVD-0.2.png").exact(), 300):
        print"[info] Results from LVL1 are ready!"
        logging.info("[info] Results from LVL1 are ready!")
    else:
        print"[error] Results from LVL1 are NOT ready!"
        logging.error("[error] Results from LVL1 are NOT ready!")
        exit(1)
        
    click("Admin-CG5-GlobalBtn-160428-VVD-0.1.png")
    wait("Admin-CG5-LevelBtn-160428-VVD-0.1.png")
    click()
    wait("Admin-CG5-Levels-LVL2Btn-160428-VVD-0.1.png")
    click(Pattern("Admin-CG5-Levels-LVL2Btn-160428-VVD-0.1.png").targetOffset(64,12))
    if exists("Admin-CG5-Levels-LVL2Activated-160428-VVD-0.1.png"):
        print"[success] level 2 has been activated!"
        logging.info("[success] level 2 has been activated!")
    else:
        print"[error] Level 2 has not been activated as expected!"
        logging.error("[error] Level 2 has not been activated as expected!")
        exit(1)
    