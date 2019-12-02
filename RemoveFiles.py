import re,os
from tqdm import tqdm
import numpy as np


def remove_UnnecessaryFile(i):
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.audit ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.bnd ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.dxf ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.eio ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.end ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.err".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.mdd ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.mtd ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.rdd ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.sln ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.rvaudit ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}out.shd ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}tbl.htm ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}ssz.csv ".format(i))
    os.system("del /f 5ZoneFanCoilDOASCool_{0}zsz.csv ".format(i))

for day in range(50,100):
    for hr in range(8,22):
        os.chdir(r"C:\Users\hvac\Desktop\FANFENG\HrOfTheYear{0}".format(day*24+hr))
        
        
        if os.path.exists("5ZoneFanCoilDOASCool_39out.mtd".format(day*24+hr)):
            print("HrOfTheYear{0}".format(day*24+hr))
            for i in range(40):
                remove_UnnecessaryFile(i)
        