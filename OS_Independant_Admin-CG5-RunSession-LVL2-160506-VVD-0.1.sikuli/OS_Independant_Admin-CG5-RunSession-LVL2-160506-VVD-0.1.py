import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Admin runs session LVL2...")

if Settings.isLinux() or Settings.isWindows():
    click("1463484752556.png")
    if exists(Pattern("1463484849979.png").similar(0.90), FOREVER):
        print"[info] End score level 2 reached!"
        logging.info("[info] End score level 2 reached!")
        click("1463485096929.png")
        click(Pattern("1463485135465.png").targetOffset(72,12))
        print"[info] Level 3 activated..."
        logging.info("[info] Level 3 activated...")
        
elif Settings.isMac():
    print"WIP - MAC not scripted yet!"

else:
    print"OS error!"