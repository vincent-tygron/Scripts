import logging;reload(logging)
FORMAT="%(asctime)-8s%(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info]===== Starting a saved SP session and check for original custom assets ====="
logging.info("[info]===== Starting a saved SP session and check for original custom assets =====")

#openApp("C:\Users\Vincent\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
#wait("1458739770583.png",10)
#dragDrop(Pattern("1459518307992.png").targetOffset(261,-121),Pattern("1459518307992.png").targetOffset(-268,-122))
#type(Key.BACKSPACE)
#paste(Pattern("1458739802503.png").targetOffset(-3,-122),"qaautotest1@tygron.com")
#paste(Pattern("1458739802503.png").targetOffset(-4,-64),"autotest1qa")
#click(Pattern("1458739802503.png").targetOffset(-6,47))
wait("1460633635395.png",10)
click()
click("1460641593403.png")
paste("1459843581563.png", "Sikulix-asset test")
click("1460018241382.png")
click("1460641654546.png")
click("1460641654546.png")
wait("1459843660197.png", 20)
click(Pattern("1459843660197.png").targetOffset(510,444))
wait("1459843727619.png", 10)
click(Pattern("1459843727619.png").targetOffset(497,447))
wait("1459865710169.png", 10)
click(Pattern("1459843936726.png").targetOffset(491,445))
wait("1459856734167.png", 5)
click(Pattern("1459856734167.png").targetOffset(-679,-164))
click(Pattern("1459856791864.png").targetOffset(477,421))
wait("1459856846963.png", 10)
click(Pattern("1459856846963.png").targetOffset(482,428))
#wait("1459865838192.png", 10)
if exists("1459844937113.png", 30):
    print"[success] Action menu icon is correct!"
    logging.info("[success] Action menu icon is correct!")
else:
    print"[error] Action menu icon is incorrect!"
    logging.error("[error] Action menu icon is incorrect!")
#click(Pattern("1459865888903.png").targetOffset(688,-221))
click("1462198091873.png")

if not exists(Pattern("1459857456018.png").similar(0.95), 5):
    print"[error] Custom function image not present!"
    logging.error("[error] Custom function image not present!")
else:
    print"[success] Custom function image is present!"
    logging.info("[success] Custom function image is present!")
click(Pattern("1459857545681.png").targetOffset(447,-144))
wait(2)
click("1459856949620.png")
if exists("1459845155856.png", 5):
    print"[success] Stakeholder icon is correct!"
    logging.info("[success] Stakeholder icon is correct!")
else:
    print"[error] Stakeholder icon is incorrect!"
    logging.error("[error] Stakeholder icon is incorrect!")
click(Pattern("1459857000605.png").targetOffset(235,-307))
if exists("1464350736716.png", 5):
    print"[success] Indicator icon is correct!"
    logging.info("[success] Indicator icon is correct!")
else:
    print"[error] Indicator icon is incorrect!"
    logging.error("[error] Indicator icon is incorrect!")

click("1460633790994.png")
if exists("1459845343814.png", 5):
    print"[success] Excel indicator output is correct!"
    logging.info("[success] Excel indicator output is correct!")
else:
    print"[error] Excel indicator output is incorrect!"
    logging.error("[error] Excel indicator output is incorrect!")
click(Pattern("1460018917955.png").targetOffset(451,-351))
type(Key.ESC)
wait("1459929967952.png", 5)
click(Pattern("1459929967952-1.png").targetOffset(-4,-84))
wait("1459930064559.png", 2)
click(Pattern("1459930064559.png").targetOffset(-2,227))
waitVanish(Pattern("1459930064559.png").targetOffset(-2,227), 15)

print"[info]===== Ending a saved SP session ====="
logging.info("[info]===== Ending a saved SP session =====")