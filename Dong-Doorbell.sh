#!/bin/bash

echo "Strating the doorbell app"

# A shell script which checks if the required python apps are running, if they are not it restarts them, and it keeps the console clean of outputs from the assosiated processes

while :
do
    if [[ $(ps aux | grep dawnreading.py | grep -v grep) ]]; then
        :
    else
        nohup python dawnreading.py > /dev/null 2>&1 &
    fi

    if [[ $(ps aux | grep dong.py | grep -v grep) ]]; then
        :
    else
        nohup python3 dong.py > /dev/null 2>&1 &
    fi
done
