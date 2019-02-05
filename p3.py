#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import mysql.connector
from random import randint

PIN_TRIGGER = 4
PIN_ECHO = 17
mydb = mysql.connector.connect(
  host="wastemgmt.cwzqmidbioqe.ap-south-1.rds.amazonaws.com",
  user="root",
  passwd="target123",
  database="wasteCollection"
)
while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    print("Waiting for sensor to settle")

    time.sleep(2)

    print("Calculating distance")

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)
    pulse_start_time=time.time()
    pulse_end_time=time.time()
    while GPIO.input(PIN_ECHO)==0:
        pulse_start_time = time.time()
    while GPIO.input(PIN_ECHO)==1:
        pulse_end_time = time.time()

    pulse_duration = pulse_end_time - pulse_start_time
    distance = round(pulse_duration * 17150, 2)
    print(int(distance))
    val1 = int(distance);
    val2 = randint(0, 100);
    val3 = randint(0, 100);

    mycursor = mydb.cursor()

    sql = "INSERT INTO RawData (cap1,cap2,cap3) VALUES (%s, %s, %s)"
    val = (val1,val2,val3)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    
    
    time.sleep(5)
    GPIO.cleanup()



