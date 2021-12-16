#!/bin/bash

mkdir turtle_tank_handout

cp challenge/*.py turtle_tank_handout
rm turtle_tank_handout/levels.py
cp levels_handout.py turtle_tank_handout/levels.py

zip -r turtle_tank_handout.zip turtle_tank_handout
rm -rf turtle_tank_handout
