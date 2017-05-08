import mysql.connector
from mysql.connector import errorcode
import time
query1 = ("select id from rawPulse order by id decs limit 1;")
query2 = ("insert into pulse(noofunit, totalCost, currentCount, lastUnitCount, nextUnitCount) valuse (%s,%s,%s,%s,%s);")

#geting initial data from the data base. 

	

IMP = 3000
costPerUnit = 15
unit = 0
totalCost = 0
nextUnitCount = IMP
lastUnitCount = 0
currentCount = 0

query1 = ("SELECT id FROM rawPulse ORDER BY id DESC LIMIT 1;")
#query2 = ("INSERT INTO pulse(noofunit, totalCost, currentCount, lastUnitCount, nextUnitCount) VALUSE(%s,%s,%s,%s,%s);")

try:    
    while True:
	cnx = mysql.connector.connect(
		user= 'root',
		passwd = 'toor',
		database = 'auth'
		)
	cursor = cnx.cursor()
	cursor.execute(query1)
	data = cursor.fetchone()
	currentCount = data[0]
	print currentCount
	if currentCount >= nextUnitCount:
		unit += 1
		totalCost += costPerUnit * unit
		nextUnitCount += IMP
		print("Unit = {} Total cost= {} NextCount at {}".format(unit,totalCost,nextUnitCount))
		time.sleep(20)

	cursor.close()
	cnx.close()
	time.sleep(.2)   

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("some thing is wrong access denied!!")
    else:
            print(err)
