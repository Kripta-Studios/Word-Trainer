#!/usr/bin/python

# MADE BY: Jinsku Kripta form Kripta-Studios,
# it's under the Mozilla Public License
# (ɔ) 2022

from random import seed
from random import randint
import csv
from time import time

seed(time)
valueCol = randint(0, 5)
valueRow = randint(1,35)

with open('Adverbien-Alemán.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == valueRow:
            if ((valueCol+1) % 2) == 0:
                print(f'{row[valueCol]} (deut)')
            else:
                print(f'{row[valueCol]} (eng)')
            solution = str(input("Solution: "))
            solution = solution.strip()
            solution = solution.lower()

            if ((valueCol+1) % 2) == 0:
                if (solution == row[valueCol - 1]):
                    print("RICHTIG => ", row[valueCol -1], row[valueCol])
                else:
                    print("FALSCH => ", row[valueCol -1], row[valueCol])
            else:
                if (solution == row[valueCol+1]):
                    print("RICHTIG => ", row[valueCol], row[valueCol +1])
                else:
                    print("FALSCH => ", row[valueCol], row[valueCol +1])
                        
                        
        line_count += 1
