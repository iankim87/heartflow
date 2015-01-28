import os, csv

#source_dir = r"R:\For_Ian\OQ2_Final"
def compute(destination_dir):

    #filename = "FFRData.txt"
    #filename = input("Enter the name of the file you would like to copy")

    # Go to active directory
    os.chdir(destination_dir)

    data = csv.reader(open("list.csv","rb"), delimiter=",")

    for row in data:
        print row
        value1 = row[0]
        print value1
        #value2 = row[1]
        #print value2

        if os.path.exists(os.path.join(destination_dir, value1)):
            continue

        os.mkdir(os.path.join(destination_dir, value1))

if __name__ == '__main__':
    compute(r"R:\For_Ian\v2.0_Workstation\FFRct_Extraction\v1.4_OQ\test")