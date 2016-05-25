import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="Wizard-Timings-test.log", level=logging.DEBUG)

logging.info("[info] Create new project 'SikuliX-Editor', don't save and exit...")

#App.open("C:\Users\Tygron\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
#wait("1458821531951.png",30)
#dragDrop(Pattern("1459500265389.png").targetOffset(256,-120), Pattern("1459500265389.png").targetOffset(-283,-126))
#type(Key.BACKSPACE)
#paste(Pattern("1458821531951.png").targetOffset(-5,-121),"qaautotest1@tygron.com")
#paste(Pattern("1458821531951.png").targetOffset(-12,-66),"autotest1qa")
#click(Pattern("1458821531951.png").targetOffset(-5,48))
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
#wait("1458822970279.png",150)

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

#sleep(2)
find("1458822999918.png")
click("1458822999918.png")
wait("1463753669378.png", 10)
click()
wait("1463753720993.png",10)
click()


