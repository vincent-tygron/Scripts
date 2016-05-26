import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="test.log", level=logging.DEBUG)

print"=====[info] Start Smoketest====="
logging.info("=====[info] Start Smoketest=====")

runScript("./OS_Independant_Engine_Independant_ ReStart-160525-VVD-0.2.sikuli")
runScript("./OS_Independant_LogOn-160419-VVD-0.5.sikuli")
runScript("./WizardNew-160503-VVD-0.1.sikuli")
runScript("./OS_Independant_Engine_Independant_ ReStart-160525-VVD-0.2.sikuli")
runScript("./OS_Independant_LogOn-160419-VVD-0.5.sikuli")
runScript("./LoadProject-160324-VVD-0.1.sikuli")
runScript("./RemoveSelectedStakeholders-160324-VVD-0.1.sikuli")
runScript("./RemoveAddPlayableStakeholders-160324-VVD-0.1.sikuli")
runScript("./RemoveAddNonPlayableStakeholders-160325-VVD-0.1.sikuli")
runScript("./CreateMeasureWithMessageAsEvent-060329-VVD-0.1.sikuli")
runScript("./ExitWithoutSaving-160324-VVD-0.1.sikuli")
runScript("./OS_Independant_Engine_Independant_ ReStart-160525-VVD-0.2.sikuli")
runScript("./OS_Independant_LogOn-160419-VVD-0.5.sikuli")
runScript("./RemoveProject-160411-VVD-0.2.sikuli")
runScript("./SignOutFromMainMenu-160324-VVD-0.1.sikuli")
runScript("./RemoveStoredValue-160525-VVD-0.1.sikuli")

print"=====[info] End Smoketest====="
logging.info("=====[info] End Smoketest=====")