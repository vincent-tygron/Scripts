import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"=====[START] Remove test projects====="
logging.info("=====[START] Remove test projects=====")

wait("1463563812283.png")
click()
wait("1463563844994.png")
click()
#hover(Pattern("1463564370399.png").similar(0.88))

for x in range (0, 120):
    Region(480,325,992,33)
    if exists("1463564361223.png", x):
        delete = find("1463565493503.png").right().find(Pattern("1463565409687.png").similar(0.54))
        click(delete)
        wait("1463564576301.png")
        click()
        print"[info] Instance %d of autotest projects has been removed!" % (x+1)
        logging.info("[info] Instance %d of autotest projects has been removed!" % (x+1))
        loc = SCREEN.getCenter()
        wheel(loc, WHEEL_DOWN, 1)
        wait(1)
        break

if not exists("1463564361223.png"):
    print"[success] All instances of autotest projects removed!"
    logging.info("[success] All instances of autotest projects removed!")
else:
    print"[error] One or more instances of autotest projects still remain!"
    logging.error("[error] One or more instances of autotest projects still remain!")
    exit(1)
    

