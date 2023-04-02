import csv

# writing csv file

data = [['Name', 'Age', 'City'], ['Subhash', '22', 'Lucknow'], ['Brij', '20', 'Lucknow']]

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
    
# now need to read write content

with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
