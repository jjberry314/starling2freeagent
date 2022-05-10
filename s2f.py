#!/usr/bin/env python3

import csv
import sys
import os

def convertCSV(filename):
    with open(filename, "rt") as source, open("fa-" + os.path.basename(filename), 'w', newline='') as result:
        rdr = csv.reader(source)
        wtr = csv.writer(result, delimiter=',', escapechar=';', quoting=csv.QUOTE_NONE)
        next(rdr)  # Skip CSV headers
        for row in rdr:
            # Skip blank lines
            if (len(row) < 4):
                continue
                
            # Skip opening balance if it is present
            if (row[0] == "" and row[1] == "Opening Balance"):
                continue
            
            # row[0] = Date
            # row[1] = Counter Party
            # row[2] = Reference
            # row[3] = Type
            # row[4] = Amount
            # row[5] = Balance
            # row[6] = Spending Category
            # row[7] = Notes
            desc = [row[3].strip(), ': ', row[1].strip(), ' [ref: ', row[2].strip(), ']']
            if (len(row) > 6): # check it's the newer format before trying to access this column
                desc.append(' ' + row[7])
            wtr.writerow([row[0], row[4], "".join(desc).strip()])

def main(argv):
    convertCSV(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])
