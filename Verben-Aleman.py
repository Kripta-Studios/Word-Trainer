#!/usr/bin/python

# MADE BY: Jinsku Kripta form Kripta-Studios,
# it's under the Mozilla Public License
# (ɔ) 2022

from random import seed
from random import randint
import csv
from time import time

seed(time)
valueCol = randint(0, 1)
valueRow = randint(1,570)

with open('Verbos-irregulares.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == valueRow:
            if valueCol == 0:
                print(f'{row[valueCol]} (span)')
            else:
                print(f'{row[valueCol]} (deut)')
            solution = str(input("Solution: "))
            solution = solution.strip()
            solution = solution.lower()

            if valueCol == 0:
                if (solution == row[valueCol+1]):
                    print("RICHTIG => ", row[valueCol +1], row[valueCol], row[2],row[3], row[4])
                else:
                    print("FALSCH => ", row[valueCol +1], row[valueCol], row[2], row[3], row[4])
            else:
                if (solution == row[valueCol-1]):
                    print("RICHTIG => ", row[valueCol], row[valueCol -1], row[2], row[3], row[4])
                else:
                    print("FALSCH => ", row[valueCol], row[valueCol -1], row[2], row[3], row[4])
                        
                        
        line_count += 1
