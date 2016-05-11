import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

print"[info] Play Level 2..."
logging.info("[info] Play Level 2...")

if Settings.isLinux() or Settings.isWindows():

    ################
    # Municipality #
    ################

    if exists("1462975903681.png", 0):
        pass

    ##############
    # Waterboard #
    ##############
    elif exists("1462975283856.png", 0):
        pass
       
    #######
    # SSH #
    #######
    elif exists("1462964850731.png", 0):
        print"[info] SSH will now perform actions in LVL2..."
        logging.info("[info] SSH will now perform actions in LVL2...")

        # Build student housing with green roof
        click("1462964532757.png")
        click("1462965017051.png")
        dragDrop(Pattern("1462969596032.png").targetOffset(-342,-36), Pattern("1462969596032.png").targetOffset(354,36))
        click("1462965284753.png")
        click("1462965316481.png")
        click("1462965356299.png")            
        click("1462965423643.png")
        click("1462965505087.png")
        print"[info] Construction planned and permit requested..."
        logging.info("[info] Construction planned and permit requested...")
        wait("1462967015724.png", FOREVER)
        print"[info] Permit approved!"
        logging.info("[info] Permit approved!")
        click()
        
        wait("1462967117443.png", 1)
        click()
        print"[info] Waiting for construction to start..."
        logging.info("[info] Waiting for construction to start...")
        wait("1462968082813.png")
        waitVanish("1462968082813.png", FOREVER)
        print"[info] Construction started!"
        logging.info("[info] Construction started!")
        
        wait("1462971096960.png", FOREVER) # WIP!!!!
        print"[success] Construction completed!"
        logging.info("[success] Construction completed!")
        
        
        
                
    ###################
    # UNI Real Estate #
    ###################

    else:
        pass
        
elif Settings.isMac():

    ################
    # Municipality #
    ################
    if exists("1462975511142.png", 0):
        
    # Confirming build permit requests
        wait(Pattern("Multiplayer-CG5-MAC-Municipality-LVL1-MiniMap-QMarkIcon-160428-VVD-0.1.png").similar(0.80), FOREVER)
        for x in range(0, 15):
            while exists(Pattern("Multiplayer-CG5-MAC-Municipality-LVL1-MiniMap-QMarkIcon-160428-VVD-0.1.png").similar(0.80), x):
                click()
                exists("Multiplayer-CG5-MAC-Municipality-LVL1-ConfMenu-YesBtn-160428-VVD-0.1.png")
                click()
                break        
        
    ##############
    # Waterboard #
    ##############
    elif exists("1462976000265.png", 0):
        pass
        
    #######
    # SSH #
    #######
    elif exists("1462976939123.png", 0):
        pass
        
    ###################
    # UNI Real Estate #
    ###################
    else:
        pass
        
else:
    print"[error] OS error!"
    logging.error("[error] OS error!")
    exit(1)

