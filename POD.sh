#!/bin/bash
while true; do
  nmap -p $2 $1 > /dev/null &
  sleep 1
done
