import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"=====[info] (Re)Start selected engine====="
logging.info("=====[info] (Re)Start selected engine=====")

engines = ("Tygron Engine Test", "Tygron Engine Preview", "Tygron Engine 2016")

########################################################
# Check if engine instance to use is already stored... #
########################################################

#def instance(value=None):#Define default value
#Sikulix.prefLoad("instance")#load.
selected = Sikulix.prefLoad("instance")
if selected == "":#if default       
    selected = select("Please select which engine to test", options = engines)#Select engine
    Sikulix.prefStore("instance", selected)#store

#print selected

#############################
# Check which OS is used... #
#############################

import subprocess
myVer = Settings.getOSVersion()
#exit(2)
#####################
# If OS is Linux... #
#####################

if Settings.isLinux():
    print "[info] Linux %s detected!" % (myVer)
    logging.info("[info] Linux %s detected!" % (myVer))
    if selected == engines[0]:
        subprocess.Popen(["/home/tygron/Desktop/Tygron Engine Test/Tygron Engine Test.sh"])
    elif selected == engines[1]:
        subprocess.Popen(["/home/tygron/Desktop/Tygron Engine Preview/Tygron Engine Preview.sh"])
    elif selected == engines[2]:
        subprocess.Popen(["/home/tygron/Desktop/Tygron Engine 2016/Tygron Engine 2016.sh"])
#    else:
#        exit(1)

#######################
# If OS is Windows... #
#######################

elif Settings.isWindows():
    #exit(2)
    print"[info] Windows %s detected!" % (myVer)
    logging.info("[info] Windows %s detected!" % (myVer))
    if selected == engines[0]:
        subprocess.Popen(["C:\Users\Vincent\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe"])
        #subprocess.Popen(["C:\Users\Tygron\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe"])
    elif selected == engines[1]:
        subprocess.Popen(["C:\Users\Vincent\AppData\Local\Tygron Engine Preview\Tygron Engine Preview.exe"])
        #subprocess.Popen(["C:\Users\Tygron\AppData\Local\Tygron Engine Preview\Tygron Engine Preview.exe"])
    elif selected == engines[2]:
        subprocess.Popen(["C:\Users\Vincent\AppData\Local\Tygron Engine 2016\Tygron Engine 2016.exe"])
        #subprocess.Popen(["C:\Users\Tygron\AppData\Local\Tygron Engine 2016\Tygron Engine 2016.exe"])
#    else:
#        exit(1)
        
########################
# If OS is MacOS(X)... #
########################

elif Settings.isMac():
    print"[info] Mac OSX %s detected!" % (myVer)
    logging.info("[info] Mac OSX %s detected!" % (myVer))
    if selected == engines[0]:
        App.open("Finder")
        click("1461066980956.png")    
        doubleClick("1460109683894.png")
    
        if exists("1458652391503.png", 3):
            click(Pattern("1458652391503.png").targetOffset(145,62))
            
    elif selected == engines[1]:
        App.open("Finder")
        click("1461066980956.png")    
        doubleClick("1461151858330.png")
    
        if exists("1458652391503.png", 3):
            click(Pattern("1458652391503.png").targetOffset(145,62))
    elif selected == engines[2]:
        App.open("Finder")
        click("1461066980956.png")    
        doubleClick("1461151873855.png")
    
        if exists("1458652391503.png", 3):
            click(Pattern("1458652391503.png").targetOffset(145,62))
#    else:
#        exit(1)
            
else:
    print "Unsupported OS detected!"
    logging.error("[error] Unsupported OS detected!")
    exit(1)

###############################
# Check if AUT has started... #
###############################

wait(3)
if exists("1460109797811.png", 2) or exists("1460111982242.png", 2):
    print "[success] Engine started!" 
    logging.info("[success] Engine started!")
    #exit(1)
else:
    print "[error] Engine not started!"
    logging.error("[error] Engine not started!")
    exit(1)

print"=====[info] Selected engine (re)started!====="
logging.info("=====[info] Selected engine (re)started!=====")