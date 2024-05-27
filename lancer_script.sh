#!/bin/bash

HEURE_ACTUELLE=$(date +%H)
cd /home/mangeoire/Documents/programmes
if [ $HEURE_ACTUELLE -ge 9 ] && [ $HEURE_ACTUELLE -le 18 ]; then
	python3 programme_v1.py
fi
