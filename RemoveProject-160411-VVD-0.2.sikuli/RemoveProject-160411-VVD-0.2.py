import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

logging.info("[info] Remove a project from the domain and verify if so afterwards...")

click("1460633738804.png")
wait("1460641451936.png",5)
click()
for x in range(0,120):
    while not exists(Pattern("1459503134043.png").similar(0.89).targetOffset(430,-1),x):
        loc = SCREEN.getCenter()
        wheel(loc,WHEEL_DOWN,5)
        wait(3)
        break
click(Pattern("1459503134043.png").similar(0.89).targetOffset(430,-1))
wait("1458830476198.png",5)
click(Pattern("1458830476198.png").targetOffset(74,48))
waitVanish(Pattern("1459503134043.png").similar(0.91),5)
if exists(Pattern("1459503134043.png").similar(0.90)):
    print("[error] Project deletion failed!")
    logging.error("[error] Project deletion failed!")
    exit(1)
else:
    print("[success] Project deletion successful!")
    logging.info("[success] Project deletion successful!")