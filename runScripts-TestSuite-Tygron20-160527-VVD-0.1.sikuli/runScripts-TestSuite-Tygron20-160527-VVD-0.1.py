import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"[info]===== Start test suite 3 ====="
logging.info("[info]===== Start test suite 3 =====")

runScript("./OS_Independant_Engine_Independant_ ReStart-160525-VVD-0.2.sikuli")
runScript("./OS_Independant_LogOn-160419-VVD-0.5.sikuli")


print"[info]===== End test suite 3 ====="
logging.info("[info]===== End test suite 3 =====")