import logging; reload(logging)
FORMAT=("%(asctime) -8s %(message) s")
logging.basicConfig(format=FORMAT, filename="testLog.txt", level=logging.DEBUG)

logging.info("[info] Admin runs session LVL2...")

if Settings.isLinux() or Settings.isWindows():

elif Settings.isMac():
    print"WIP - MAC not scripted yet!"

else:
    print"OS error!"