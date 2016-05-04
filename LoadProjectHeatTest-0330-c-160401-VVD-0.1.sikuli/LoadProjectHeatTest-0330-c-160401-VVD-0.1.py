import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

logging.info("[info] Load project Heat test-0330-c...")

click("1460625139975.png")
wait("1458823588830.png",10)
paste("1460535580366.png", "Heat test-0330-c")
waittime = 0.5
for x in range(0, 30):
    if exists("1459510584427.png", waittime):
        print '[success] Found project in %d seconds' % (x*waittime)
        logging.info('[success] Found project in %d seconds' % (x*waittime))
        break
if not exists("1459510584427.png"):
    print '[error] Project not found!'
    logging.error('[error] Project not found!')
    exit(1)
else:
    click(Pattern("1459510626139.png").targetOffset(-2,-10))
#wait("1458823826086.png"#,60)
waittime = 0.5
for x in range(0, 120):
    if exists("1459510749106.png", waittime):
        print '[success] Loading project in %d seconds' % (x*waittime)
        break
if not exists(Pattern("1459510749106.png").similar(0.81)):
    print("[error] Loading project failed!")
    logging.error("[error] Loading project failed!")
    exit(1)
else:
    print("[success] loading project successful!")
    logging.info("[success] Loading project successful!")



