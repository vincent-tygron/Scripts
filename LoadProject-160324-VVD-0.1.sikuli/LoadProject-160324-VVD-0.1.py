import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info] Load previously saved project..."
logging.info("[info] Load previously saved project...")

click("1460629295497.png")
wait("1458823588830.png",10)
paste("1460535580366.png", "Sikulix-editor")
waittime = 1
for x in range(0, 30):
    if exists("1459500798531.png", waittime):
        print '[success] Found project in %d seconds' % (x*waittime)
        logging.info('[success] Found project in %d seconds' % (x*waittime))
        break
click(Pattern("1459500817932.png").targetOffset(-16,-99))

#waittime = 1
for x in range(0, 120):
    if exists("1458829978984.png", x):
        print"[success] Loading project in %d seconds successful!" % x
        logging.info("[success] Loading project in %d seconds successful!" % x)
        break

if not exists("1458829978984.png"):
    print("[error] Loading project failed after %d seconds!"  % (x))
    logging.error("[error] Loading project failed after %d seconds!"  % (x))
    exit(1)



