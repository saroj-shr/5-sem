import mysql.connector
from mysql.connector import errorcode
import time
import serial

ser = serial.Serial('/dev/ttyACM0',9600)

try:
    cnx = mysql.connector.connect(
        user = 'root',
        passwd = 'toor',
        database = 'test'
    )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("some thing is wrong")
    else:
            print(err)

else:
	cursor = cnx.cursor()
	query = ("INSERT INTO pulse(minValue, count) VALUES(%s,%s);")
	while True:
		time_stamp = time.strftime("%y/%m/%d %H:%M:%S ",time.localtime())
	        read_serial = ser.readline().split(" ")
        	print time_stamp + read_serial[0] + " " + read_serial[1]
    		data = (read_serial[0],read_serial[1])
    		cursor.execute(query,data)
    		cnx.commit()
