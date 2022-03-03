# Task: from a supplied CSV, create a new file for individual store numbers
# In the each store file, list comma delimited SKUs and price with a 5% discount
# Print the run time and lines processed to the console

import csv
import timeit

file = 'in.csv'

discount = .05

lines_processed = 1


def calc_price(old_price: float):
    this_discount = old_price * discount
    #Return float as a string to limit to 2 decimal places
    return "{:.2f}".format(old_price - this_discount)


start = timeit.default_timer()

with open(file) as f:
    dictReader = csv.DictReader(f)
    processedStoreNo = ""
    for row in dictReader:
        rowToWrite = []
        if processedStoreNo is not row['Store'] and processedStoreNo != "":
            newFile.close()
        rowToWrite.append(row['Sku'])
        rowToWrite.append(calc_price(float(row['Price'])))

        with open(row['Store'] + ".csv", 'a', newline='') as newFile:
            writer = csv.writer(newFile)
            writer.writerow(rowToWrite)

        rowToWrite.clear()
        processedStoreNo = row['Store']
        lines_processed += 1
    newFile.close()
f.close()

stop = timeit.default_timer()
print('Run Time: ', stop - start, ' Lines processed: ', lines_processed)
