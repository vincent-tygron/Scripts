import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info] Remove and add a playable stakeholder..."
logging.info("[info] Remove and add a playable stakeholder...")

click("1460555150006.png")
click("1458823866614-1.png")
click("1458825780294.png")
find("1458826491175.png")
click("1458826491175.png")
click("1458824021110.png")
wait("1458824117807.png",5)
click(Pattern("1458824117807.png").targetOffset(91,46))
waitVanish("1458826593271.png",10)
if exists("1458826593271.png"):
    print("[error] Stakeholder (playable) not removed!")
    logging.error("[error] Stakeholder (playable) not removed!")
    exit(1)
else:
   print("[success] Stakeholder (playable) removed!")
   logging.info("[success] Stakeholder (playable) removed!")
click("1458826637062.png")
find("1458826491175.png")
click("1458826491175.png")
wait("1458826697965.png",5)
click(Pattern("1458826697965.png").targetOffset(-129,-5))
wait("1458826845109.png",5)
if not exists("1458826845109.png"):
    print("[error] Stakeholder (playable) not added!")
    logging.error("[error] Stakeholder (playable) not added!")
    exit(1)
else:
   print("[success] Stakeholder (playable) added!")
   logging.info("[success] Stakeholder (playable) added!")
