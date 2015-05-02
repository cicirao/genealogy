import csv

with open('force.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  names = []
  for row in reader:
    if row[0] not in names:
      names.append(row[0])
    if row[1] not in names:
	  names.append(row[1])
  print names

with open('names.csv', 'wb') as csvfile:
	writer = csv.writer(csvfile, delimiter=' ')
	for name in names:
	  writer.writerow(name)

