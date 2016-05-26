import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)
print"[info] Create measure with message as event..."
logging.info("[info] Create measure with message as event...")
logging.info("[info] Create a message first...")

click("1460555283350.png")
click("1459245066009.png")
click(Pattern("1459245139622.png").targetOffset(-792,455))

if not exists("1459245189675.png",10):
    print("[error]Unable to find newly created message!")
    logging.error("[error]Unable to find newly created message!")
    exit(1)
else:
    print("[success] Default message created!")
    logging.info("[success] Default message created!")
logging.info("[info] Fill in message details...")
click("1459245189675.png")
wait("1459245373316.png",5)
click(Pattern("1459245373316.png").targetOffset(-130,-241))
dragDrop(Pattern("1459245564572.png").targetOffset(-25,-254), Pattern("1459245564572.png").targetOffset(-138,-254))
paste("L Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui.")
type(Key.ENTER)
dragDrop(Pattern("1459245807956.png").targetOffset(13,-392), Pattern("1459245807956.png").targetOffset(-135,-392))
paste("Test Message")
type(Key.ENTER)
logging.info("[info] Create a default Measure...")
click("1460555856951.png")
click("1459247969569.png")
click(Pattern("1459248105788.png").targetOffset(-124,28))
if not exists("1459248136506.png",5):
    print("[error] Unable to find default Measure!")
    logging.error("[error] Unable to find default Measure!")
    exit(1)
else:
    print("[success] Default Measure created!")
    logging.info("[success] Default Measure created!")

print"[info]Assign message to default measure..."
logging.info("[info]Assign message to default measure...")
click("1459248136506.png")
dragDrop(Pattern("1459248998362.png").targetOffset(-55,-90), Pattern("1459248998362.png").targetOffset(-135,-90))
paste("Test Maatregel")
type(Key.ENTER)
click(Pattern("1459249087146.png").targetOffset(-20,-1))
wait("1459248460442.png",5)
click(Pattern("1459248460442.png").targetOffset(-98,392))
wait("1459248524434.png",5)
click("1459248524434.png")
wait("1459248561651.png",5)
dragDrop(Pattern("1459248583514.png").targetOffset(95,-59), Pattern("1459248583514.png").targetOffset(97,-7))
#exists(Pattern("1459248630731.png").targetOffset(95,-14))
wait("1459248658234.png")
click("1459248658234.png")
wait("1459248709986.png",5)
click(Pattern("1459248729130.png").targetOffset(262,76))
if not exists("1459249421115.png"):
    print("[error] Failed to attach message to measure!")
    logging.error("[error] Failed to attach message to measure!")
    exit(1)
else:
    print("[success] Succeeded to attach message to measure!")
    logging.info("[success] Succeeded to attach message to measure!")

print"[info]Create default action menu..."
logging.info("[info]Create default action menu...")
click("1459249168163.png")
click(Pattern("1459249202130.png").targetOffset(-125,16))
find("1459324358998.png")
paste("1459324358998.png", "New action menu")
type(Key.ENTER)
if not exists("1459325109149.png",5):
    print("[error] Unable to locate 'New action menu'!")
    logging.error("[error] Unable to locate 'New action menu'!")
    exit(1)
else:
    print("[success] 'New action menu'  has been created and verified!")
    logging.info("[success] 'New action menu'  has been created and verified!")
click("1459325149781.png")
#Region(12,209,137,49)
if not exists("1459325301101.png",5):
    print("[error] Unable to expand 'New action menu'!")
    logging.error("[error] Unable to expand 'New action menu'!")
else:
    print("[success] 'New action menu' has been expanded to show 'Assigned actions'!")
    logging.info("[success] 'New action menu' has been expanded to show 'Assigned actions'!")
wait("1459326125461.png")

print"[info] Changing Action menu image..."
logging.info("[info] Changing Action menu image...")
click("1459249793282.png")
wait("1459249847875.png")
click(Pattern("1459249847875.png").targetOffset(20,-127))
click(Pattern("1459249904435.png").targetOffset(101,246))
if not exists("1459249959843.png"):
    print("[error] Failed to change action menu image!")
    logging.error("[error] Failed to change action menu image!")
else:
    print("[success] Succeeded to change action menu image!")
    logging.info("[success] Succeeded to change action menu image!")

print"[info] Assigning Test Measure with Test Message to Test Action menu..."
logging.info("[info] Assigning Test Measure with Test Message to Test Action menu...")
#Click somewhere on empty space to remove highlight of image
click("1459327011621.png")
dragDrop(Pattern("1459326453454.png").targetOffset(-27,-391), Pattern("1459326453454.png").targetOffset(-135,-394))
paste("Test")
type(Key.ENTER)
click("1459325586053.png")
click("1459325600949.png")
click("1459250123595.png")
click("1459250161362.png")
click("1459250181746.png")
if not exists("1459250372881.png",5):
    print("[error] Assigning measure to action menu failed!")
    logging.error("[error] Asasigning measure to action menu failed!")
    exit(1)
else:
    print("[success] Assigning measure to action menu successful!")
    logging.info("[success] Assigning measure to action menu successful!")
find("1459250481658.png")
click("1459250481658.png")
wait("1459250523762.png",5)
click(Pattern("1459250523762.png").targetOffset(75,180))
click(Pattern("1459250604347.png").targetOffset(77,179))
click(Pattern("1459250638827.png").targetOffset(115,-186))
click("1459250742346.png")
click(Pattern("1459250762299.png").targetOffset(-10,-145))
if not exists("1459250815819.png"):
    print("[error] Message as measure failed!")
    logging.error("[error] Message as measure failed!")
    exit(1)
else:
    print("[success] Message as measure successful!")
    logging.info("[success] Message as measure successful!")
click(Pattern("1459250815819.png").targetOffset(156,147))
click(Pattern("1459250974178.png").targetOffset(116,-185))
click("1459251021978.png")


                




