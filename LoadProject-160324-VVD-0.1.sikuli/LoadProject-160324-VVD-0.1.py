import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info] Load previously saved project..."
logging.info("[info] Load previously saved project...")

click("1460629295497.png")
wait("1458823588830.png",10)
paste("1460535580366.png", "Sikulix-editor")
waittime = 0.5
for x in range(0, 30):
    if exists("1459500798531.png", waittime):
        print '[success] Found project in %d seconds' % (x*waittime)
        logging.info('[success] Found project in %d seconds' % (x*waittime))
        break
click(Pattern("1459500817932.png").targetOffset(-16,-99))

if not exists("1458829978984.png", 60):
    print("[error] loading project failed!")
    logging.error("[error] Loading project failed!")
    exit(1)
else:
    print("[success] loading project successful!")
    logging.info("[success] Loading project successful!")



