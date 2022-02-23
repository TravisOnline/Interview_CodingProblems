#Task: from a supplied CSV, create a new file for individual store numbers
#In the each store file, list comma delimited SKUs and price with a 5% discount

import csv

file = 'in.csv'

discount = .05


def calc_price(old_price: float):
    this_discount = old_price * discount
    #Return float as a string to limit to 2 decimal places
    return "{:.2f}".format(old_price - this_discount)


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
    newFile.close()
f.close()
