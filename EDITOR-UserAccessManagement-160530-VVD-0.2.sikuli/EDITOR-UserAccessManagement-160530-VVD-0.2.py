import logging;reload(logging)
FORMAT="%(asctime)-8s%(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info] >>>>>>>>>> Start EDITOR User Rights Test <<<<<<<<<<"
logging.info("[info] >>>>>>>>>> Start EDITOR User Rights Test <<<<<<<<<<")

#App.open("C:\Users\Vincent\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
wait("1458739770583.png",10)
#dragDrop(Pattern("1459518307992.png").targetOffset(261,-121),Pattern("1459518307992.png").targetOffset(-268,-122))
#type(Key.BACKSPACE)
paste(Pattern("1458739802503.png").targetOffset(-3,-122),"qaautotest1@tygron.com")
type(Key.TAB)
paste("autotest1qa")
click(Pattern("1458739802503.png").targetOffset(-6,47))
wait("1460643987762.png",10)
click()
click(Pattern("1460644168289.png").targetOffset(70,80))
wait("1460033347283.png")
dragDrop("1460033362763.png", "1460033366795.png")
click(Pattern("1460033410387.png").similar(0.79))
click("1460035871962.png")
click(Pattern("1460033535050.png").targetOffset(-43,13))
if exists("1460037143441.png"):
    print("[success] User was changed to EDITOR!")
    logging.info("[success] User was changed to EDITOR!")
else:
    print("[error] User was not changed to EDITOR!")
    logging.error("[error] User was not changed to EDITOR!")
    exit(1)
click("1460033748728.png")
wait("1460036378215.png", 3)
paste(Pattern("1458739802503-1.png").targetOffset(-3,-122),"qaautotest2@tygron.com")
type(Key.TAB)
paste("autotest2qa")
click(Pattern("1458739802503.png").targetOffset(-6,47))
if exists("1460644871163.png"):
    print("[success] EDITOR access is correct!")
    logging.info("[success] EDITOR access is correct!")
else:
    print("[error] EDITOR access is not as expected!")
    logging.error("[error] EDITOR access is not as expected!")
    exit(1)
click("1460033748728.png")
wait("1460036378215.png", 3)
#click(Pattern("1460034167361.png").targetOffset(807,-495))
#waitVanish(Pattern("1460034167361.png").targetOffset(807,-495))

print"[info] >>>>>>>>>> End EDITOR User Rights Test <<<<<<<<<<"
logging.info("[info] >>>>>>>>>> End EDITOR User Rights Test <<<<<<<<<<")