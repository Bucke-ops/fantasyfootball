import csv

# Download latest version
path = "fantasy_merged_7_17.csv"

rows = []
with open(path, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)
        
# printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:10]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')