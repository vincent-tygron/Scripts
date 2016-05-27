import logging;reload(logging)
FORMAT="%(asctime)-8s%(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info]===== Remove asset test project ====="
logging.info("[info]===== Remove asset test project =====")

#wait("1460634955425.png", 5)

#openApp("C:\Users\Vincent\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
#wait("1458739770583.png",10)
#dragDrop(Pattern("1459518307992.png").targetOffset(261,-121),Pattern("1459518307992.png").targetOffset(-268,-122))
#type(Key.BACKSPACE)
#paste(Pattern("1458739802503.png").targetOffset(-3,-122),"qaautotest1@tygron.com")
#paste(Pattern("1458739802503.png").targetOffset(-4,-64),"autotest1qa")
#click(Pattern("1458739802503.png").targetOffset(-6,47))
wait("1460632925176.png",10)
click()
wait("1460640646906.png", 5)
click()
wait("1459932415342.png", 5)

for x in range (0,120):
    while not exists("1459933047665.png", 1):
        loc=SCREEN.getCenter()
        wheel(loc,WHEEL_DOWN,5)
        wait(1)
        break

if exists("1460465181376.png"):
    print("[success] Project 'Sikulix-asset Test' has been found!")
    logging.info("[success] Project 'Sikulix-asset Test' has been found!")
else:
    print("[error] Unable to find project 'Sikulix-asset Test'!")
    logging.error("[error] Unable to find project 'Sikulix-asset Test'!")
    exit(1)

delete = find(Pattern("1460465181376.png").similar(0.80)).right().find("1460466665380.png")
for x in range(0, 10):
    while exists("1460465181376.png", x):
        click(delete)
        wait("1459933743589.png")
        click(Pattern("1459933743589.png").targetOffset(88,50))
        print"[success] Instance %d of project 'Sikulix-asset Test' has been removed!" % (x+1)
        logging.info("[success] Instance %d of project 'Sikulix-asset Test' has been removed!" % (x+1))
        loc=SCREEN.getCenter()
        wheel(loc,WHEEL_DOWN,1)
        wait(1)
        break

if not exists("1460465181376.png"):
    print("[success] All instances of project 'Sikulix-asset Test' has been removed!")
    logging.info("[success] All instances of project 'Sikulix-asset Test' has been removed!")
else:
    print("[error] Project 'Sikulix-asset Test' is still present?")
    logging.error("[error] Project 'Sikulix-asset Test' is still present?")
    exit(1)
#click(Pattern("1460639461962.png").similar(0.90).targetOffset(43,-22))

click(Pattern("1462193203579.png").similar(0.67))

print"[info]===== Remove asset test project completed ====="
logging.info("[info]===== Remove asset test project completed =====")