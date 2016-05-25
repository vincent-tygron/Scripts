import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

logging.info("[info] Log in with username and password...")

openApp("C:\Users\Tygron\AppData\Local\Tygron Engine Test\Tygron Engine Test.exe")
wait("1458821531951.png",10)
dragDrop(Pattern("1459500265389.png").targetOffset(256,-120), Pattern("1459500265389.png").targetOffset(-283,-126))
type(Key.BACKSPACE)
paste(Pattern("1458821531951.png").targetOffset(-5,-121),"qaautotest1@tygron.com")
paste(Pattern("1458821531951.png").targetOffset(-12,-66),"autotest1qa")
click(Pattern("1458821531951.png").targetOffset(-5,48))
if not exists("1460632903740.png", 5):
    print("[error] log in failed!")
    logging.error("[error] log in failed!")
    exit(1)
else:
    print"[success] log in successful!"
    logging.info("[success] Log in successful!")
