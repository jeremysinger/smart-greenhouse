#!/bin/bash

for I in {1..10}
do
  DATA=`python humidity.py | grep -v incorrect | grep temp | cut -d' ' --output-delimiter=',' -f1,2,4,6 | sed 's/,/ /'`
  sleep 1
  LIGHT_DATA=`python light.py`
  if [ -n "$DATA" ]
  then 
    echo $DATA,$LIGHT_DATA
  fi
done

