#!/usr/bin/python
import os

# This is the package that allows us to control and interact with the GPIO pins, without this package we wouldn’t be able to talk with our distance sensor.
import RPi.GPIO as GPIO

# CThis package allows us to control time-related functions with the script. We mainly just use this to put the script to sleep and also time how long it takes to receive data back from the sensor.
import time

# MySQL driver written in Python
import mysql.connector

# for random values
from random import randint

# Requests is the HTTP library for Python for SMS API
import requests

# This is length of empty dust bin
BIN_DIST1=19.0

# This is url of SMS API fast2sms
url = "https://www.fast2sms.com/dev/bulk"

PIN_TRIGGER = 23

PIN_ECHO = 24

# mysql connection information
mydb = mysql.connector.connect(
  host=os.getenv("DB_HOST", "your-db-host"),
  user=os.getenv("DB_USER", "your-db-user"),
  passwd=os.getenv("DB_PASSWORD", "your-db-password"),
  database=os.getenv("DB_NAME", "your-db-name")
)

# INFINITE LOOP OF CHECKING
while True:

	# set our GPIO mode to GPIO.BOARD, this means we are using the physical pin numbers and not the BCM numbers. 
    GPIO.setmode(GPIO.BCM)

    # set trigger pin as output pin
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    
    # set echo pin as input pin
    GPIO.setup(PIN_ECHO, GPIO.IN)

    # GPIO.LOW does not send anything to sensor This ensures we should be getting more consistent readings.
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    print("Waiting for sensor to settle")
    # We then proceed to sleep the script for 2 seconds to ensure we give the distance sensor enough time to settle and don’t immediately start triggering it.
    time.sleep(2)

    print("Calculating distance")

    # gets trigger pin to send signal to sensor
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    # Sensor needs 1 nanosecond to trigger it
    time.sleep(0.00001)

    # Immediately after the sleep has completed, we set PIN_TRIGGER low again.
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    # Initialize time variables to garbage values
    pulse_start_time=time.time()
    pulse_end_time=time.time()

    # we run a while loop to continually check if PIN_ECHO is low (0) if it is we continually set the pulse_start_time to the current time until it becomes high (1)
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()

    # once ECHO pin reads HIGH we record the time
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()
    
    # difference between pulse_end_time and pulse_start_time
    pulse_duration = pulse_end_time - pulse_start_time

    # With the pulse duration calculated we can work out the distance, it traveled since we know the rough speed of ultrasonic sound is 34300 cm/s.
    # Since the duration of the pulse is the time it took for the ultrasonic sound to hit an object and bounce back, we will just use half the speed to calculate the distance it traveled before returning. Doing this is a simpler calculation then calculating the distance with the full speed then dividing by 2.
    distance = round(pulse_duration * 17150, 2)
    
    # print(distance)
    
    # check if the input reading is valid
    if distance < BIN_DIST1 :
        #print(int(distance))
        #val1=distance

        # distance to percentage
        val1 = int((BIN_DIST1-distance)/BIN_DIST1*100)
        print(val1)

        # Random Values
        val2 = randint(0, 100)
        # val2 = 91
        val3 = randint(0, 100);

        # recording current timstamp to send to database for stats
        val4=time.strftime('%Y-%m-%d %H:%M:%S')

        #  cursor() method is used to instantiate a MySQLCursor object
        mycursor = mydb.cursor()

        # SQL QUERY 
        sql = "INSERT INTO RawData2 (Cap1,Cap2,Cap3,timestp) VALUES (%s, %s, %s, %s)"
        
        # readings of dustbin and time
        val = (val1,val2,val3,val4)

        # This method executes the given database operation
        mycursor.execute(sql, val)

        # This method sends a COMMIT statement to the MySQL server, committing the current transaction.
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        # checking if the dustbin are above limit
        if(val1>90 or val2>90 or val3>90):
            listBins=[]
            if(val1>90):
                listBins.append("bin1")
            if(val2>90):
                listBins.append("bin2")
            if(val3>90):
                listBins.append("bin3")
            
            msg = " ".join(listBins)

            # message that needs to send to driver
            realmsg = "Please Collect The Garbage From "+ msg
            # print(realmsg)

            # querystring for the SMS API
            querystring = {
                    "authorization": os.getenv("SMS_AUTH_TOKEN"),
                    "sender_id": "FSTSMS",
                    "message": realmsg,
                    "language": "english",
                    "route": "p",
                    "numbers": os.getenv("DEFAULT_TEST_NUMBER")
            }

            # headers for SMS API GET request
            headers = {
                'cache-control': "no-cache"
            }

            # sending GET REQUEST to SMS API
            response = requests.request("GET", url, headers=headers, params=querystring)

            # printing respose from the SMS API Server
            print(response.text)


    # to clean up all the ports you’ve used. 
    GPIO.cleanup()

    # sleep for x seconds before checking again
    time.sleep(5)
    
