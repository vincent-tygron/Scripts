import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info] Attempt to remove currently selected stakeholder and verify message flow..."
logging.info("[info] Attempt to remove currently selected stakeholder and verify message flow...")

exists("1460555150006.png", 5)
click()
exists("1458823866614.png", 5)
click()
exists("1458825780294.png")
click()
wait(Pattern("1458823942061.png").similar(0.71).targetOffset(-17,-1),10)
find(Pattern("1458823942061.png").similar(0.71).targetOffset(-17,-1))
click(Pattern("1458823942061.png").similar(0.71).targetOffset(-17,-1))
wait("1458823988831.png",15)
click("1458824021110.png")
wait("1458824117807.png",5)
sleep(2)
click(Pattern("1458824117807.png").targetOffset(91,46))
wait("1458824217454.png",5)
if not exists("1458824217454.png"):
    print("[error] Can't find asset")
    logging.error("[error] Can't find asset")
    exit(1)
else:
    print("[success] Unable to delete selected stakeholder, correct message is displayed!")
    logging.info("[success] Unable to delete selected stakeholder, correct message is displayed!")
click(Pattern("1458824217454.png").targetOffset(230,48))
click("1458825461431.png")
wait("1458825487063.png",5)
