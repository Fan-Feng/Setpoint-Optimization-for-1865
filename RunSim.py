import re,os
from tqdm import tqdm
import numpy as np
import pandas as pd


def convert_DayOfTheYear_ToMOnAndDay(dayOfTheYear):
    dy = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(12):
        if sum(dy[:i+1])>= dayOfTheYear:
            month = i+1
            day = dayOfTheYear - sum(dy[:i])
            break
        else:
            continue
    return month,day


def weekday(dayOfTheYear):
    Weekdays = ["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"]
    idx = dayOfTheYear%7
    return Weekdays[idx]

def generate_idf(day,hr,SetPoint,i):#substitude_Value
    with open("5ZoneFanCoilDOASCool_template.idf") as fp:
        idf_str = fp.read()
        idf_str = re.sub("%DayOfYear%",str(day),idf_str)
        if day<= 7:
            EndDay = 7
        else:
            EndDay = day
        
        idf_str = re.sub("%StartMon%",str(convert_DayOfTheYear_ToMOnAndDay(EndDay-6)[0]),idf_str)
        idf_str = re.sub("%StartDay%",str(convert_DayOfTheYear_ToMOnAndDay(EndDay-6)[1]),idf_str)
        idf_str = re.sub("%EndMon%",str(convert_DayOfTheYear_ToMOnAndDay(EndDay)[0]),idf_str)
        idf_str = re.sub("%EndDay%",str(convert_DayOfTheYear_ToMOnAndDay(EndDay)[1]),idf_str)
        idf_str = re.sub("%Weekday%",weekday(EndDay),idf_str)
        
        
        idf_str = re.sub("%Hour%",str(hr),idf_str)
        idf_str = re.sub("%SetPoint_Value%",str(SetPoint),idf_str)
        if not os.path.exists("HrOfTheYear{0}".format(day*24-24+hr)):
            os.mkdir("HrOfTheYear{0}".format(day*24-24+hr))
        with open(r"HrOfTheYear{0}/5ZoneFanCoilDOASCool_{1}.idf".format(day*24-24+hr,i),"w+") as fp1:
            fp1.write(idf_str)

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

start = 346
end = 350

os.chdir(r"E:\SetPoint_Opt\BrutalForce")
for day in range(start,end):
    for hr in range(8,22):
        if not os.path.exists("HrOfTheYear{0}".format(day*24+hr)):
            #print(day*24+hr)
            for i,SP in enumerate(range(100,140)):
                SetPoint = (SP/2-32)/1.8
                generate_idf(day+1,hr,SetPoint,i)   

for day in range(start,end):
    for hr in range(8,22):
        for i in range(40):
            os.chdir(r"E:\SetPoint_Opt\BrutalForce\HrOfTheYear{0}".format(day*24+hr))
            os.system(r"C:\EnergyPlusV9-1-0\energyplus.exe -w C:\EnergyPlusV9-1-0\WeatherData\USA_IL_Chicago-OHare.Intl.AP.725300_TMY3.epw -p 5ZoneFanCoilDOASCool_{0} -r 5ZoneFanCoilDOASCool_{0}.idf ".format(i))
            remove_UnnecessaryFile(i)
        
