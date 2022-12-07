#!/bin/bash

if [ $# -lt 2 ]; then
    echo "Not enough arguments provided. Try running again with ./create_day.sh year day"
    exit 1
fi

year=$1
day=$2

cd ./Solutions/$year/
mkdir $day
cp ../../templates/* ./$day
touch $day/instructions.md
touch $day/input.txt
touch $day/example1.txt
