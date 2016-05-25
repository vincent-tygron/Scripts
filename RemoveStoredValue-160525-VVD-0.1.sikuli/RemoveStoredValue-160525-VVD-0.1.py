import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"=====[info] Removing stored value====="
logging.info("=====[info] Removing stored value=====")

Sikulix.prefRemove()

print"Stored value removed!"
logging.info("Stored value removed!")
