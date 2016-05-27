import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info] Create new project 'SikuliX-Editor', don't save and exit..."
logging.info("[info] Create new project 'SikuliX-Editor', don't save and exit...")

wait("1460535966422.png", 30)
click()
wait("1458822263448.png",10)
paste(Pattern("1458822263448.png").targetOffset(-24,-222),"SikuliX-Editor")
click(Pattern("1458822358415.png").targetOffset(-15,-53))
click("1458822423703.png")
wait("1458822546599.png",10)
click(Pattern("1458822563767.png").targetOffset(226,11))
wait("1458822622398.png",10)
paste(Pattern("1458822661143.png").targetOffset(-215,-157),"Arnhem")
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
