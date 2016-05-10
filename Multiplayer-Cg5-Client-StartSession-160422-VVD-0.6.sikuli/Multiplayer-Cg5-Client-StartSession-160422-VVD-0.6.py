import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

logging.info("[info] Accept invite and load Cg5 session...")

if Settings.isLinux() or Settings.isWindows():
    wait("Multiplayer-Client-SplashScreen-ContinueBtn-160422-VVD-0.1.png", FOREVER)
    click()
    if exists("Multiplayer-Client-Cg5-ExplanationScreen-160422-VVD-0.1.png", 60):
        print"[success] Client is proceeding into session setup!"
        logging.info("[success] Client is proceeding into session setup!")
    else:
        print"[error] Client did not proceed to session setup (in time)!"
        logging.error("[error] Client did not proceed to session setup (in time)!")
        exit(1)

    click("Multiplayer-Client-SplashScreen-ContinueBtn2-160422-VVD-0.1.png")
    if not exists("Multiplayer-Client-TeamName-FilledIn-160422-VVD-0.1.png", 3):
        type("Multiplayer-Client-TeamName-Blank-160422-VVD-0.1.png", "QA")
    Region(805,541,874,467)
    click("Multiplayer-Client-SesionName-ContinueBtn3-160422-VVD-0.1.png")
    wait("Multiplayer-Client-StakeholderPanelTitle-160422-VVD-0.1.png", 15)
    click(Pattern("Multiplayer-Client-StakeholderSelectionList-160422-VVD-0.1.png").targetOffset(-32,-122))
    exists("Multiplayer-Client-StakeholderSelection-ChooseStakeholderBtn-160422-VVD-0.1.png", 1)
    click()
    if not exists("Multiplayer-Client-AssignmentPanelTitle-160422-VVD-0.1.png"):
        click("Multiplayer-Client-StakeholderSelection-Waterboard-160425-VVD-0.1.png")
        exists("Multiplayer-Client-StakeholderSelection-ChooseStakeholderBtn-160422-VVD-0.1.png", 1)
        click()
        if not exists("Multiplayer-Client-AssignmentPanelTitle-160422-VVD-0.1.png"):
            click("Multiplayer-Client-StakeholderSelection-SSH-160425-VVD-0.1.png")
            exists("Multiplayer-Client-StakeholderSelection-ChooseStakeholderBtn-160422-VVD-0.1.png", 1)
            click()
            if not exists("Multiplayer-Client-AssignmentPanelTitle-160422-VVD-0.1.png"):
                click("Multiplayer-Client-StakeholderSelection-UniRealEstate-160425-VVD-0.1.png")

                click("Multiplayer-Client-StakeholderSelection-ChooseStakeholderBtn-160422-VVD-0.1.png")

    wait("Multiplayer-Client-AssignmentPanelTitle-160422-VVD-0.1.png", 10)
    click("Multiplayer-Client-SplashScreen-ContinueBtn2-160422-VVD-0.1.png")

if Settings.isMac():
    wait("Multiplayer-Client-MAC-SplashScreen-ContinueBtn-160425-VVD-0.1.png", FOREVER)
    click()
    if exists("Multiplayer-Client-MAC-Cg5-ExplanationScreen-160425-VVD-0.1.png", 60):
        print"[success] Client is proceeding into session setup!"
        logging.info("[success] Client is proceeding into session setup!")
    else:
        print"[error] Client did not proceed to session setup (in time)!"
        logging.error("[error] Client did not proceed to session setup (in time)!")
        exit(1)

    click("Multiplayer-Client-MAC-SplashScreen-ContinueBtn2-160425-VVD-0.1.png")
    if not exists("Multiplayer-MAC-Client-TeamName-FilledIn-160425-VVD-0.1.png", 3):
        type("Multiplayer-Client-MAC-TeamName-Blank-160425-VVD-0.1.png", "QA")
    Region(805,541,874,467)
    click("Multiplayer-Client-MAC-SesionName-ContinueBtn3-160425-VVD-0.1.png")
    wait("Multiplayer-Client-MAC-StakeholderPanelTitle-160425-VVD-0.1.png", 15)
    click(Pattern("Multiplayer-Client-MAC-StakeholderSelectionList-160425-VVD-0.1.png").targetOffset(-17,-89))
    exists("Multiplayer-Client-MAC-StakeholderSelection-ChooseStakeholderBtn-160425-VVD-0.1.png", 1)
    click()
    if not exists("Multiplayer-Client-MAC-AssignmentPanelTitle-160425-VVD-0.1.png"):
        click("Multiplayer-Client-MAC-StakeholderSelection-Waterboard-160426-VVD-0.1.png")
        exists("Multiplayer-Client-MAC-StakeholderSelection-ChooseStakeholderBtn-160425-VVD-0.1.png", 1)
        click()
        if not exists("Multiplayer-Client-MAC-AssignmentPanelTitle-160425-VVD-0.1.png"):
            click("Multiplayer-Client-MAC-StakeholderSelection-SSH-160426-VVD-0.1.png")
            exists("Multiplayer-Client-MAC-StakeholderSelection-ChooseStakeholderBtn-160425-VVD-0.1.png", 1)
            click()
            if not exists("Multiplayer-Client-MAC-AssignmentPanelTitle-160425-VVD-0.1.png"):       
                click("Multiplayer-Client-MAC-StakeholderSelection-UniRealEstate-160426-VVD-0.1.png")
                click("Multiplayer-Client-MAC-StakeholderSelection-ChooseStakeholderBtn-160425-VVD-0.1.png")

    wait("Multiplayer-Client-MAC-AssignmentPanelTitle-160425-VVD-0.1.png", 10)
    click("Multiplayer-Client-MAC-SplashScreen-ContinueBtn2-160425-VVD-0.1.png")