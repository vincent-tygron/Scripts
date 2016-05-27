import logging;reload(logging)
FORMAT="%(asctime)-8s%(message)s"
logging.basicConfig(format=FORMAT, filename="testlog.log", level=logging.DEBUG)

logging.info("=====Starting an SP session and check for original custom assets=====")

openApp("C:\Users\Vincent\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
wait("1458739770583.png",10)
dragDrop(Pattern("1459518307992.png").targetOffset(261,-121),Pattern("1459518307992.png").targetOffset(-268,-122))
type(Key.BACKSPACE)
paste(Pattern("1458739802503.png").targetOffset(-3,-122),"qaautotest1@tygron.com")
paste(Pattern("1458739802503.png").targetOffset(-4,-64),"autotest1qa")
click(Pattern("1458739802503.png").targetOffset(-6,47))
wait("1460631537714.png",10)
click()
click("1460641111390.png")
paste("1459843581563.png", "Sikulix-asset test")
click("1460018241382.png")
wait("1459843660197.png", 30)
click(Pattern("1459843660197.png").targetOffset(510,444))
wait("1459843727619.png", 30)
click(Pattern("1459843727619.png").targetOffset(497,447))
wait("1459843785573.png", 30)
paste(Pattern("1459843785573.png").targetOffset(-414,-252), "AssetTest")
click(Pattern("1459843936726.png").targetOffset(491,445))
wait("1459856734167.png", 5)
click(Pattern("1459856734167.png").targetOffset(-679,-164))
click(Pattern("1459856791864.png").targetOffset(477,421))
wait("1459856846963.png", 10)
click(Pattern("1459856846963.png").targetOffset(482,428))
#wait("1459856895256.png", 10)
if exists("1459844937113.png", 30):
    print"[success] Action menu icon is correct!"
    logging.info("[success] Action menu icon is correct!")
else:
    print"[error] Action menu icon is incorrect!"
    logging.error("[error] Action menu icon is incorrect!")
click()
wait("1459857157300.png", 3)
click(Pattern("1459857157300.png").targetOffset(82,280))
wait("1459857234202.png", 3)
click(Pattern("1459857234202.png").targetOffset(82,284))
wait("1459857284019.png", 3)
click(Pattern("1459857284019.png").targetOffset(137,-290))
find("1459857337210.png")
click(Pattern("1459857337210.png").targetOffset(13,0))
if not exists("1459857456018.png", 5):
    print"[error] Custom function image not present!"
    logging.error("[error] Custom function image not present!")
    exit(1)
else:
    print"[success] Custom function image is present!"
    logging.info("[success] Custom function image is present!")
click(Pattern("1459857545681.png").targetOffset(447,-144))
waitVanish("1459857571744.png", 3)
click("1459856949620.png")
if exists("1459845155856.png", 5):
    print"[success] Stakeholder icon is correct!"
    logging.info("[success] Stakeholder icon is correct!")
else:
    print"[error] Stakeholder icon is incorrect!"
    logging.error("[error] Stakeholder icon is incorrect!")
click(Pattern("1459857000605.png").targetOffset(235,-307))
if exists("1460460826086.png", 5):
    print"[success] Indicator icon is correct!"
    logging.info("[success] Indicator icon is correct!")
else:
    print"[error] Indicator icon is incorrect!"
    logging.error("[error] Indicator icon is incorrect!")
click(Pattern("1460460826086.png").targetOffset(-46,1))
if exists("1459845343814.png", 5):
    print"[success] Excel indicator output is correct!"
    logging.info("[success] Excel indicator output is correct!")
else:
    print"[error] Excel indicator output is incorrect!"
    logging.error("[error] Excel indicator output is incorrect!")
click(Pattern("1460017398574.png").targetOffset(450,-353))
type(Key.ESC)
wait("1459929967952.png", 2)
click(Pattern("1459929967952.png").targetOffset(-1,-32))
if exists("1459858035949.png", 2):
    print"[success] Session saved!"
    logging.info("[success] Session saved!")
else:
    print"[error] Project did not save (in time)!"
    logging.error("[error] Project did not save (in time)!")
    exit(1)
click(Pattern("1459858035949.png").targetOffset(129,36))
click(Pattern("1459929967952.png").targetOffset(-4,-84))
wait("1459930064559.png", 2)
click(Pattern("1459930064559.png").targetOffset(-2,227))
waitVanish(Pattern("1459930064559.png").targetOffset(-2,227), 15)

logging.info("=====Ending/ saving an SP session with original custom assets=====")