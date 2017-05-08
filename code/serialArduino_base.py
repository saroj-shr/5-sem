import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)

while True:
	time_stamp = time.strftime("%y/%m/%d %H:%M:%S ",time.localtime())
	read_serial = ser.readline().split(" ")	
	print time_stamp + read_serial[0] + " " + read_serial[1]
