#!/bin/bash
#for i in {2..81}
#do
#    mkdir $i
#done

while true
do
    for i in {2..81}
    do
	wget -O $i-$(date +%Y-%m-%d-%H:%M).jpg -U "google-chrome" "https://www.medellin.gov.co/simm/camaras-cctv/imagen$i.jpg"
    done
    sleep 60
done
