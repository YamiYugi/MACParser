#!/bin/bash

echo "Starting Daily Network Analysis. Wiping previous Log File for storage purposes"
echo " " > /root/Desktop/Final/log.txt 
tcpdump -e > /root/Desktop/Final/log.txt
