import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info] Create new 1x1km project, exit without saving..."
logging.info("[info] Create new 1x1km project, exit without saving...")

if Settings.isWindows():
    if exists("1472026626431.png", 30):
        n = find("1472026626431.png")
        n.highlight(1)
        n.click()
        print'[success] Starting New Project Wizard'
        logging.info('[success] Starting New Project Wizard')
    else:
        print'[error] Unable to start New Project Wizard!'
        logging.error('[error] Unable to start New Project Wizard!')
        exit(1)
if Settings.isLinux():
    if exists("1472026626431.png", 30):
        click()
        print'[success] Starting New Project Wizard'
        logging.info('[success] Starting New Project Wizard')
    else:
        print'[error] Unable to start New Project Wizard!'
        logging.error('[error] Unable to start New Project Wizard!')
        exit(1)
r = Region(499,185,682,679)
if r.exists("1472026339898.png",10):
    print'[success] New Project Wizard Started'
    logging.info('[success] New Project Wizard Started')
else:
    print'[error] New Project Wizard NOT started (in time?)'
    logging.error('[error] New Project Wizard NOT started (in time?)')
    exit(1)
if Settings.isWindows():
    if r.exists("1472027347019.png", 30):
        f = r.find("1472027347019.png")
        f.highlight(1)
        f.paste("Win-1x1km-test")
if Settings.isLinux():
    if r.exists("1472027347019.png", 30):
        f = r.find("1472027347019.png")
        f.paste("Lin-1x1km-test")

print'[info] Set language to Dutch...'
logging.info('[info] Set language to Dutch...')
r = Region(513,390,634,172)
if not r.exists (Pattern("1472032291175.png").similar(0.94)):
    r.click(Pattern("1472032337947.png").similar(0.90))
    r.click("1472032396387.png")
    if r.exists (Pattern("1472032291175.png").similar(0.95)):
        print'[success] Language set to Dutch'
        logging.info('[success] Language set to Dutch') 
    else:
        print'[error] Language NOT set to Dutch!'
        logging.error('[error] Language NOT set to Dutch!')
        exit(1)

click("1472037669429.png")
if Settings.isWindows():
    if exists("1472037775588.png"):
        f = find("1472037876476.png")
        f.highlight(1)
        f.paste("Den Haag")
        type(Key.ENTER)
        if exists("1472037998245.png", 10):
            d = find("1472037998245.png")
            d.highlight(1)
            print'[success] Map focus set to The Hague'
            logging.info('[success] Map focus set to The Hague')           
if Settings.isLinux():
    if exists("1472037775588.png"):
        paste("1472037876476.png", "Den Haag")
        type(Key.ENTER)
        if exists("1472037998245.png", 10):
            print'[success] Map focus set to The Hague'
            logging.info('[success] Map focus set to The Hague')        
    
exit(200)
        
paste(Pattern("1458822263448.png").targetOffset(-24,-222),"SikuliX-Wiz1x1km")
click(Pattern("1458822358415.png").targetOffset(-15,-53))
click("1458822423703.png")
wait("1458822546599.png",10)
click(Pattern("1458822563767.png").targetOffset(226,11))
wait("1458822622398.png",10)
paste(Pattern("1458822661143.png").targetOffset(-215,-157),"Den Haag")
type(Key.ENTER)
wait("1458822737716.png",30)
click(Pattern("1458822780840.png").targetOffset(411,303))

waittime = 1
for x in range(0, 1200):
    if exists("1458829978984.png", waittime):
        print'[success] creating project in %d seconds was successful!' % (x*waittime)
        logging.info('[success] Creating project in %d seconds was successful!' % (x*waittime))
        break
    
if not exists("1458829978984.png", waittime):
    print'[error] creating project failed after %d seconds!' % (x*waittime)
    logging.error('[error] creating project failed after %d seconds!' % (x*waittime))
    exit(1)

find("1458822999918.png")
click("1458822999918.png")
wait("1463753669378.png", 10)
click()
wait("1463753720993.png",10)
click()
waitVanish("1458822999918.png", 60)
if not exists("1458822999918.png"):
    print"[success] Exit project succesfull!"
    logging.info("[success] Exit project succesfull!")
else:
    print"[error] Project did not exit in time!"
    logging.error("[error] Project did not exit in time!")
    exit(1)
