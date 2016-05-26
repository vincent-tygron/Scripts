import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info] Remove,change and add a non-playable stakeholder..."
logging.info("[info] Remove, change and add a non-playable stakeholder...")

find("1458909532322.png")
click(Pattern("1458909532322.png").targetOffset(-83,-15))
if not exists("1458913652706.png",5):
    print("[error] Adding stakeholder failed!")
    logging.error("[error] Adding stakeholder failed!")
    exit(1)
else:
    print("[success] Adding stakeholder successful!")
    logging.info("[success] Adding stakeholder successful!")
click("1458913652706.png")
click("1458909935497.png")
click(Pattern("1458910006618.png").targetOffset(-110,-23))
if not exists("1458910089946.png",5):
    print("[error] Changing default stakeholder failed!")
    logging.error("[error] Changing default stakeholder failed!")
    exit(1)
else:
    print("[success] Changing default stakeholder successful!")
    logging.info("[success] Changing default stakeholder successful!")
click("1458910189882.png")
click("1458910221283.png")
click("1458910266322.png")
click("1458910292577.png")
wait("1458913307802.png",5)
click(Pattern("1458913307802.png").targetOffset(79,49))
waitVanish("1458910396794.png",10)
if exists("1458910396794.png"):
    print("[error] Stakeholder (non playable) not removed!")
    logging.error("[error] Stakeholder (non playable) not removed!")
    exit(1)
else:
   print("[success] Stakeholder (non playable) removed!")
   logging.info("[success] Stakeholder (non playable) removed!")
