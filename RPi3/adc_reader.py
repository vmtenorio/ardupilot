# Simple program that reads from the ADC and stores it in a CSV file

import Adafruit_ADS1x15
import csv
import datetime
from mavproxy import log_paths
import os

adc = Adafruit_ADS1x15.ADS1115()

logdir,_,_ = log_paths()
logpath = os.path.join(logdir, "adc_log.csv")

csvfile = open(logpath, 'wb')
csvwriter = csv.writer(csvfile)

GAIN = 1

PIN_A0 = 0
PIN_A1 = 1
PIN_A2 = 2
PIN_A3 = 3

while True:
	now = datetime.utcnow()
	timestr = now.strftime("%Y-%m-%dT%H:%M:%S.") + (now.microseconds * 1e-06)
	value = adc.read_adc(0, gain=GAIN)
	csvwriter.writerow([timestr, str(value)])
	
