#!/bin/bash

for dir in 2..3}; do
    cd $dir
    for file in *; do
	new=$dir-$file
	#echo $new
	cp $file ../validation/$new
    done
    cd ..
done
