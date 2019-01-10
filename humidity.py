#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import datetime

PIN=4
MAXCOUNT=20
BUFLEN=50

buf = [0]*BUFLEN
st = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)
GPIO.output(PIN,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(PIN,GPIO.LOW)
time.sleep(0.02)

GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

j=0
while j<BUFLEN:
  i=0
  while i<MAXCOUNT:
    if GPIO.input(PIN)==1:
      break
    i+=1
  i=0
  while i<MAXCOUNT:
    # count how long the signal stays high
    if GPIO.input(PIN)==0:
      break
    i+=1
  buf[j] = i
  j+=1

print(str(buf))
  
HIGH_THRESHOLD=3
MAX_THRESHOLD=MAXCOUNT
for j in range(len(buf)):
  if buf[j] < HIGH_THRESHOLD or buf[j] >= MAX_THRESHOLD:
    buf[j] = 0
  else:
    buf[j] = 1

bytes = [0]*5  # 5 bytes of data

for b in range(len(bytes)):

  startIndex = b*8 + 1
  for j in range(startIndex,startIndex+8):
    bytes[b] = (bytes[b]<<1) | buf[j]

if ((bytes[0]+bytes[1]+bytes[2]+bytes[3])%256 != bytes[4]):
  print ("incorrect reading")
else:
  print("%s humidity %d temp %d\n"%(st, bytes[0],bytes[2]))
