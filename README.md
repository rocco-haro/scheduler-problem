# Scheduler
By Rocco Haro

## Requirements
* python v3.6.3
## Run
python carScheduler.py

## Problem
We have N people who arrive at location A, and need to get to location B.
Travel for a person can occur by becoming a passenger in a vehicle with C capacity.
This vehicle can hold up to C people, and there are M number of vehicles.
It is required that M*C >= N.
We know when each person will arrive, and it is given by an list of timestamps.

Find a set of car-> people(s) assignment that seeks to optimize wait time,
namely the minimal amount of wait time for a

## Solution
1) Find valid car combinations
2) Build car map with found combos
3) Find lowest wait time from car map
4) Output max wait time, cars -> peoples mapping
