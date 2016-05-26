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

delete = find("1464254840995.png").right().find(Pattern("1464182960063.png").exact())
for x in range(0, 10):
    while exists("1464179632293.png"):
        click(delete)
        wait("1458830476198.png")
        click(Pattern("1458830476198.png").targetOffset(74,48))
        print"[success] Instance %d of project was deleted!" % (x+1)
        logging.info("[success] Instance %d of project was deleted!" % (x+1))
        loc = SCREEN.getCenter()
        wheel(loc, WHEEL_DOWN, 1)
        wait(1)
        break

if exists("1464179632293.png"):
    print("[error] Project deletion failed!")
    logging.error("[error] Project deletion failed!")
    exit(1)
else:
    print("[success] Project deletion successful!")
    logging.info("[success] Project deletion successful!")