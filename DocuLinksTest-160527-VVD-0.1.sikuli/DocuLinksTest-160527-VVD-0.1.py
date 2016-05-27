import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info]===== Start Documentation links test ====="
logging.info("[info]===== Start Documentation links test =====")

if Settings.isWindows():

    click("1464352879963.png")
    paste("1464352921564.png", "Sikulix-menus-nl")
    wait("1464353709007.png", 1)
    click()

    for x in range (0, 30):
        if exists("1464353173658.png", x):
            print"[success] Project SikuliX-menus-NL loaded in %d seconds!" % x
            logging.info("[success] Project SikuliX-menus-NL loaded in %d seconds!" % x)
            break

    if not exists("1464353173658.png"):
            print"[error] Project SikuliX-menus-NL not loaded after %d seconds!" % x
            logging.error("[error] Project SikuliX-menus-NL not loaded after %d seconds!" % x)
        
    #click("1464263378772.png")#GEO data
    print"[info] Under Geo Data..."
    logging.info("[info] Under Geo Data...") 
    hover("1464263441069.png")#Constructions
    print"[info] For Constructions..."
    logging.info("[info] For Constructions...")    
    wait("1464263651642.png", 1)
    click()
    if exists("1464263853145.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464264164382.png")#Terrain
    print"[info] For Terrain..."
    logging.info("[info] For Terrain...")    
    wait("1464264311397.png", 1)
    click()
    if exists("1464264334964.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464266059746.png")#Zoning
    print"[info] For Zoning..."
    logging.info("[info] For Zoning...")    
    wait("1464266098064.png", 1)
    click()
    if exists("1464266143776.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464269640800.png")#Plots
    print"[info] For Plots..."
    logging.info("[info] For Plots...")    
    wait("1464269666599.png", 1)
    click()
    if exists("1464269686407.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")    

    hover("1464266221040.png")#Areas
    print"[info] For Areas..."
    logging.info("[info] For Areas...")    
    wait("1464266257055.png", 1)
    click()
    if exists("1464266280999.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464266397798.png")#Overlays
    print"[info] For Overlays..."
    logging.info("[info] For Overlays...")    
    wait("1464266413126.png", 1)
    click()
    if exists("1464266443158.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    click("1464266624445.png")#Stakeholders
    print"[info] Under Stakeholders..."
    logging.info("[info] Under Stakeholders...")
    
    hover("1464266789211.png")#Stakeholders
    print"[info] For Stakeholders..."
    logging.info("[info] For Stakeholders...")    
    wait("1464266806451.png", 1)
    click()
    if exists("1464266827931.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464266866315.png")#Actions
    print"[info] For Actions..."
    logging.info("[info] For Actions...")    
    wait("1464266878923.png", 1)
    click()
    if exists("1464266919906.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png") 

    hover("1464267038914.png")#Measures
    print"[info] For Measures..."
    logging.info("[info] For Measures...")    
    wait("1464267074441.png", 1)
    click()
    if exists("1464267094562.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464267161121.png")#Dike Types
    print"[info] For Dike Types..."
    logging.info("[info] For Dike Types...")    
    wait("1464267176577.png", 1)
    click()
    if exists("1464267196617.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464267378423.png")#Upgrade Types
    print"[info] For Upgrade Types..."
    logging.info("[info] For Upgrade Types...")    
    wait("1464267429055.png", 1)
    click()
    if exists("1464267444430.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464267483702.png")#Event Bundles
    print"[info] For Event Bundles..."
    logging.info("[info] For Event Bundles...")    
    wait("1464267504254.png", 1)
    click()
    if exists("1464267533998.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    click("1464268527927.png")#Indicators

    hover("1464268562439.png")#Indicators
    print"[info] For Indicators..."
    logging.info("[info] For Indicators...")    
    wait("1464268590390.png", 1)
    click()
    if exists("1464268613206.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464268673862.png")#Function Values
    print"[info] For Function Values..."
    logging.info("[info] For Function Values...")    
    wait("1464268794341.png", 1)
    click()
    if exists("1464268818092.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464269741687.png")#Globals
    print"[info] For Globals..."
    logging.info("[info] For Globals...")    
    wait("1464269765199.png", 1)
    click()
    if exists("1464269785903.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464269827606.png")#Query Tool
    print"[info] For Query Tool..."
    logging.info("[info] For Query Tool...")    
    wait("1464269861654.png", 1)
    click()
    if exists("1464269884013.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png") 

    click("1464270145779.png")#Animations

    hover("1464270204899.png")#Cinematics
    print"[info] For Cinematics..."
    logging.info("[info] For Cinematics...")    
    wait("1464270223307.png", 1)
    click()
    if exists("1464270243827.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464270344331.png")#Special Effects
    print"[info] For Special Effects..."
    logging.info("[info] For Special Effects...")    
    wait("1464270374210.png", 1)
    click()
    if exists("1464270405945.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464270439889.png")#Units
    print"[info] For Units..."
    logging.info("[info] For Units...")    
    wait("1464270448458.png", 1)
    click()
    if exists("1464270491129.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464270606409.png")#Weather
    print"[info] For Weather..."
    logging.info("[info] For Weather...")    
    wait("1464270618488.png", 1)
    click()
    if exists("1464270661648.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464270685320.png")#Environment
    print"[info] For Environment..."
    logging.info("[info] For Environment...")    
    wait("1464270696024.png", 1)
    click()
    if exists("1464270710528.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    click("1464270833519.png")#Storyline

    hover("1464270922279.png")#Levels
    print"[info] For Levels..."
    logging.info("[info] For Levels...")    
    wait("1464270977478.png", 1)
    click()
    if exists("1464271016029.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464271092477.png")#Timeline
    print"[info] For Timeline..."
    logging.info("[info] For Timeline...")    
    wait("1464271131628.png", 1)
    click()
    if exists("1464271146564.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464271172180.png")#Messages
    print"[info] For Messages..."
    logging.info("[info] For Messages...")    
    wait("1464271185109.png", 1)
    click()
    if exists("1464271203125.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    click("1464271323995.png")#Tools

    hover("1464271419051.png")#Panels
    print"[info] For Panels..."
    logging.info("[info] For Panels...")    
    wait("1464271519641.png", 1)
    click()
    if exists("1464271540249.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464271598273.png")#Screenshot
    print"[info] For Screenshot..."
    logging.info("[info] For Screenshot...")    
    wait("1464271689225.png", 1)
    click()
    if exists("1464271702448.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464271878096.png")#Video
    print"[info] For Video..."
    logging.info("[info] For Video...")    
    wait("1464271806103.png", 1)
    click()
    if exists("1464271816711.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464271940767.png")#Free Cam
    print"[info] For Free Cam..."
    logging.info("[info] For Free Cam...")    
    wait("1464272071286.png", 1)
    click()
    if exists("1464272098206.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    hover("1464272140157.png")#Api Overview
    print"[info] For Api Overview..."
    logging.info("[info] For Api Overview...")    
    wait("1464272160349.png", 1)
    click()
    if exists("1464272205996.png"):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")
    click("1464263942032.png")

    click("1464272256844.png")#Help

    hover("1464272541210.png")#Wiki
    print"[info] For Wiki..."
    logging.info("[info] For Wiki...")    
    wait("1464272553914.png", 1)
    click()
    if exists("1464272618755.png", 10):
        if exists("1464263615554.png"):
            print"[error] Documentation not written yet!"
            logging.error("[error] Documentation not written yet!")
        else:
            print"[success] Documentation is available!"
            logging.info("[success] Documentation is available!")
    else:
        print"[error] Documentation not found!"
        logging.error("[error] Documentation not found!")

    click(Pattern("1464272686794.png").targetOffset(477,-292))
    wait("1464263942032.png")
    click()
    wait("1464353520320.png")
    click()

elif Settings.isLinux():
    pass # WIP

elif Settings.isMac():
    pass # WIP

else:
    print"[error] OS error!"
    logging.error("[error] OS error!")
    exit(1)

print"[info]===== End Documentation links test ====="
logging.info("[info]===== End Documentation links test =====")