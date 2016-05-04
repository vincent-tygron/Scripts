#Use on project Heat test-0330-c only!!!

import logging;reload(logging)
FORMAT="%(asctime)-8s %(message)s"
logging.basicConfig(format=FORMAT, filename="HEAT_Timings-test.log", level=logging.DEBUG)

logging.info("===== START runScripts-HEAT_timings-160401-VVD-0.1 =====")

runScript("./OS_Independant_Engine_Independant_ Start-160503-VVD-1.6.sikuli")
runScript("./OS_Independant_LogOn-160419-VVD-0.5.sikuli")
runScript("./LoadProjectHeatTest-0330-c-160401-VVD-0.1.sikuli")
runScript("./HeatTimingTest-160414-VVD-0.2.sikuli")
runScript("./ExitWithoutSaving-160324-VVD-0.1.sikuli")
#runScript("./CloseTygronEngineTestApp-160404-VVD-0.1.sikuli")

logging.info("===== END runScripts-HEAT_timings-160401-VVD-0.1 =====")