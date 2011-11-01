#!/bin/sh

# 

for odsfile in cookedData/*.ods
do
	basename=$(basename odsfile .ods)
	python ods2csv/ssconverter.py $odsfile data/$basename-%s.csv
done

