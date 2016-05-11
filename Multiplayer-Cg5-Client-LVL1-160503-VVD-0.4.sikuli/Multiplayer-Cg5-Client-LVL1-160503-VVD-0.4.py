import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="TestLog.txt", level=logging.DEBUG)

print"[info] Play Level 1..."
logging.info("[info] Play Level 1...")

if Settings.isLinux() or Settings.isWindows():

    ################
    # Municipality #
    ################

    if exists(Pattern("1462268628697.png").similar(0.90)):
        print"[info] Municipality selected as stakeholder" 
        logging.info("[info] Municipality selected as stakeholder")
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
        
        # Renovating houses

        click("1462268826840.png")
        click(Pattern("1462268858543.png").similar(0.83))
        wait("1462268895815.png")
        click()
        wait("1462268916231.png")
        click()
        click("1462273364939.png")
        
        wait("1461669772050.png", 5)
        click()
        wait("1461669817711.png")
        dragDrop(Pattern("1461669817711.png").targetOffset(-11,-84), Pattern("1461669817711.png").targetOffset(-181,-86))
        paste("4/2/2010")
        click("1462277505883.png")
        wait("1461671232017.png", FOREVER)
        click()     
        wait("1461669963955.png")
        click()
        
        wait("1462273944361.png", FOREVER)
        for x in range(0, 15):
            while exists("1462273944361.png", x):
                click()
                exists("1461669963955.png")
                click()
                break

    ##############
    # Waterboard #
    ##############
    
    elif exists(Pattern("Multiplayer-CG5-Waterboard-LVL1-IntroPanel-160426-VVD-0.1.png").similar(0.90)):
        print"[info] Waterboard selected as stakeholder" 
        logging.info("[info] Waterboard selected as stakeholder")
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
        
        wait(Pattern("1462275915840.png").similar(0.80), 3)
        doubleClick()
        wait("1462366634006.png", 3)
        # Building something
    

        loc = SCREEN.getCenter()
        wheel(loc,WHEEL_DOWN,1)
        click("Multiplayer-CG5-Waterboard-LVL1-WaterActionMenuBtn-160426-VVD-0.1.png")
        if exists("Multiplayer-CG5-Waterboard-LVL1-OpenWaterLocation-160426-VVD-0.1.png", 5):
            dragDrop(Pattern("1461676305234.png").targetOffset(589,-287), Pattern("1461676305234.png").targetOffset(-665,301))
        else:
            print"ERROR!!!" 
            exit(1)
        click("Multiplayer-CG5-Waterboard-LVL1-WaterActionMenuYesBtn-160426-VVD-0.1.png")
        wait("1461669772050.png", 10)
        click()
        wait("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ConfPanelImage-160426-VVD-0.1.png")
        dragDrop(Pattern("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ConfPanelDate-160426-VVD-0.1.png").targetOffset(67,0), Pattern("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ConfPanelDate-160426-VVD-0.1.png").targetOffset(-105,-3))
        paste("4/2/2010")
        click("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ConfirmBtn-160426-VVD-0.1.png")
        wait("1461671232017.png", FOREVER)
        click()
        wait("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ApprovalPanel-160426-VVD-0.1.png", 3)
        click(Pattern("Multiplayer-CG5-Waterboard-LVL1-OpenWater-ApprovalPanel-160426-VVD-0.1.png").targetOffset(394,144))

    #######
    # SSH #
    #######
    
    elif exists(Pattern("1461669319306.png").similar(0.90)):
        print"[info] SSH selected as stakeholder" 
        logging.info("[info] SSH selected as stakeholder")
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
        wait("1461669563841.png", 3)
        doubleClick()
            
        # Building cheap student housing
        wait("1462356862110.png", 3)
        
        click("1461669579386.png")
        click("1461669604651.png")
        
        loc = SCREEN.getCenter()
        wheel(loc, WHEEL_DOWN, 2)
        wait(1)
        
        dragDrop(Pattern("1461670183163.png").targetOffset(-242,-46), Pattern("1461670183163.png").targetOffset(174,-5))
        click("1461669742268.png")
        wait("1461669772050.png", 5)
        click()
        wait("1461669817711.png")
        dragDrop(Pattern("1461669817711.png").targetOffset(-11,-84), Pattern("1461669817711.png").targetOffset(-181,-86))
        paste("4/2/2010")
        click("1461669963955.png")
        wait("1461671232017.png", FOREVER)
        click()
        wait("1461671253872.png")
        click("1461671279745.png")
    
    ###################
    # UNI Real Estate #
    ###################
    
    else:
    #elif exists("Multiplayer-CG5-UNI-LVL1-IntroPanel-160426-VVD-0.1.png"):
        print"[info] Uni Real Estate selected as stakeholder" 
        logging.info("[info] Uni Real Estate selected as stakeholder")
        
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
        
        wait("Multiplayer-CG5-UNI-LVL1-MiniMap1l-160426-VVD-0.1.png", 5)
        click()
            
    # Building educational building
    
        click("Multiplayer-CG5-UNI-LVL1-BuildActionMenuBtn-160426-VVD-0.1.png")
        wait("1462363508989.png", 60)
        click()
        dragDrop(Pattern("Multiplayer-CG5-UNI-LVL1-EduLuxeLocation-160426-VVD-0.1.png").targetOffset(-85,-90), Pattern("Multiplayer-CG5-UNI-LVL1-EduLuxeLocation-160426-VVD-0.1.png").targetOffset(67,78))
        click("1461669742268.png")
        wait("1461669772050.png", 5)
        click()
        wait("1461669817711.png")
        dragDrop(Pattern("1461669817711.png").targetOffset(-11,-84), Pattern("1461669817711.png").targetOffset(-181,-86))
        paste("4/2/2010")
        click("1461669963955.png")
        wait("1461671232017.png", FOREVER)
        click()
        wait("1461671253872.png")
        click("1462285025864.png")    

elif Settings.isMac():

    ################
    # Municipality #
    ################
    if exists(Pattern("Multiplayer-CG5-MAC-Municipality-LVL1-IntroPanel-160428-VVD-0.1.png").similar(0.81), 10):
        print"[info] Municipality selected on OSX as stakeholder" 
        logging.info("[info] Municipality selected on OSX as stakeholder")

        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
        
        # Upgrade housing units
        
        click("1461849752329.png")
        click(Pattern("1462284355528.png").similar(0.80))
        click("1461849333213.png")
        click("1461849365950.png")
        click("1461849396105.png")
        click(Pattern("Multiplayer-CG5-MAC-Municipality-LVL1-MiniMap-ArrowIcon-160428-VVD-0.1.png").similar(0.88))
        click("1461849822023.png")
        wait(Pattern("1461850858853.png").similar(0.87), FOREVER)
        click()
        wait("1461850895182.png", 10)
        click()        
        
#        click("1461669742268.png")
#        wait("1461669772050.png", 5)
#        click()
#        wait("1461669817711.png")
#        dragDrop(Pattern("1461669817711.png").targetOffset(-11,-84), Pattern("1461669817711.png").targetOffset(-181,-86))
#        paste("4/2/2010")
#        click("1461669963955.png")
#        wait("1461671232017.png", FOREVER)
#        click()
#        wait("1461671253872.png")
#        click("1461671279745.png") 

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
    
    elif exists(Pattern("1462541275986.png").similar(0.80)):
        print"[info] Waterboard selected on OSX as stakeholder" 
        logging.info("[info] Waterboard selected on OSX as stakeholder")
        
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
        
        wait(Pattern("1462541323201.png").targetOffset(-2,2), 3)
        doubleClick()
        wait("1462542476981.png")
                
        loc = SCREEN.getCenter()
        wheel(loc,WHEEL_UP,1)    
        
        # Building something
    
        click("1462541375880.png")
        exists("Multiplayer-CG5-MAC-Waterboard-LVL1-OpenWaterLocation-160506-VVD-0.1.png", 5)
        dragDrop(Pattern("Multiplayer-CG5-MAC-Waterboard-LVL1-OpenWaterLocation-160506-VVD-0.1.png").targetOffset(397,-214), Pattern("Multiplayer-CG5-MAC-Waterboard-LVL1-OpenWaterLocation-160506-VVD-0.1.png").targetOffset(-495,206))
        click("1462543923597.png")
        wait(Pattern("Multiplayer-CG5-MAC-Municipality-LVL1-MiniMap-ArrowIcon-160428-VVD-0.1.png").similar(0.88), 10)
        click()
        wait("Multiplayer-CG5-MAC-Waterboard-LVL1-OpenWater-ConfPanelImage-160506-VVD-0.1.png", 3)
        dragDrop(Pattern("Multiplayer-CG5-MAC-Waterboard-LVL1-OpenWater-ConfPanelDate-160506-VVD-0.1.png").targetOffset(47,0), Pattern("Multiplayer-CG5-MAC-Waterboard-LVL1-OpenWater-ConfPanelDate-160506-VVD-0.1.png").targetOffset(-105,-3))
        paste("4/2/2010")
        click("Multiplayer-CG5-MAC-Waterboard-LVL1-OpenWater-ConfirmBtn-160506-VVD-0.1.png")
        wait("1462545153790.png", FOREVER)
        click()
        wait("Multiplayer-CG5-MAC-Waterboard-LVL1-OpenWater-ConfPanelImage-160506-VVD-0.1.png", 3)
        click("Multiplayer-CG5-MAC-Waterboard-LVL1-OpenWater-ConfirmBtn-160506-VVD-0.1.png")

    #######
    # SSH #
    #######
    
    elif exists(Pattern("1461669319306.png").similar(0.90)):
        print"[info] SSH selected on OSX as stakeholder" 
        logging.info("[info] SSH selected on OSX as stakeholder")
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
        click("1461669563841.png")
            
        # Building cheap student housing
    
        click("1461669579386.png")
        click("1461669604651.png")
        dragDrop(Pattern("1461670183163.png").targetOffset(-242,-46), Pattern("1461670183163.png").targetOffset(174,-5))
        click("1461669742268.png")
        wait("1461669772050.png", 5)
        click()
        wait("1461669817711.png")
        dragDrop(Pattern("1461669817711.png").targetOffset(-11,-84), Pattern("1461669817711.png").targetOffset(-181,-86))
        paste("4/2/2010")
        click("1461669963955.png")
        wait("1461671232017.png", FOREVER)
        click()
        wait("1461671253872.png")
        click("1461671279745.png")
    
    ###################
    # UNI Real Estate #
    ###################
    
    else:
    #elif exists("Multiplayer-CG5-UNI-LVL1-IntroPanel-160426-VVD-0.1.png"):
        print"[info] Uni Real Estate selected on OSX as stakeholder" 
        logging.info("[info] Uni Real Estate selected on OSX as stakeholder")
        loc = SCREEN.getCenter()
        click(loc)
        click(loc)
        type(Key.SPACE)
        click("Multiplayer-CG5-UNI-LVL1-MiniMap1l-160426-VVD-0.1.png")
            
    # Building educational building
    
        click("Multiplayer-CG5-UNI-LVL1-BuildActionMenuBtn-160426-VVD-0.1.png")
        click("Multiplayer-CG5-UNI-LVL1-EduLuxuryBtn-160426-VVD-0.1.png")
        dragDrop(Pattern("Multiplayer-CG5-UNI-LVL1-EduLuxeLocation-160426-VVD-0.1.png").targetOffset(-85,-90), Pattern("Multiplayer-CG5-UNI-LVL1-EduLuxeLocation-160426-VVD-0.1.png").targetOffset(67,78))
        click("1461669742268.png")
        wait("1461669772050.png", 5)
        click()
        wait("1461669817711.png")
        dragDrop(Pattern("1461669817711.png").targetOffset(-11,-84), Pattern("1461669817711.png").targetOffset(-181,-86))
        paste("4/2/2010")
        click("1461669963955.png")
        wait("1461671232017.png", FOREVER)
        click()
        wait("1461671253872.png")
        click("1461671279745.png")

else:
    print"[error] OS error!"
    logging.error("[error] OS error!")
    exit(1)
    
print"[info] End Level 1..."
logging.info("[info] End Level 1...")