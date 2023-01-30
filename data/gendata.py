import csv
import random
import sys

PREFIX = sys.argv[1]
MAX_COLS = 30
NUM_COLS = random.randint(1, 30)
NUM_ROWS = random.randint(1, 100)

with open("data.csv", "w") as csvfile:
    fieldnames = []

    for col in range(0,NUM_COLS):
        fieldnames.append(PREFIX+str(col))

    writer = csv.writer(csvfile)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(NUM_ROWS):
        row = {}
        for col in fieldnames:
            row[col] = col+"_data"

        writer.writerow(row)