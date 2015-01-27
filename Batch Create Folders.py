import os, csv

destination_dir = r"R:\For_Ian\v2.0_Workstation\Lumen_Variability\v2.0\v1.4_OQ"

# Go to active directory
os.chdir(destination_dir)

data = csv.reader(open("list.csv","rb"), delimiter=",")

for row in data:
    print row
    value1 = row[0]
    print value1

    if os.path.exists(os.path.join(destination_dir, value1)):
        continue

    os.mkdir(os.path.join(destination_dir, value1))
