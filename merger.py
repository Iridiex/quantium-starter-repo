import csv
import os

def merge_csv_files(input_file1, input_file2, input_file3):
    with open(input_file1) as file1, open(input_file2) as file2, open(input_file3) as file3:
        read1 = csv.reader(file1, delimiter=',')
        read2 = csv.reader(file2, delimiter=',')
        read3 = csv.reader(file3, delimiter=',')
        next(read1)
        next(read2)
        next(read3)

        with open('merged.csv', 'w') as file:
            writer = csv.writer(file)
            for i in (read1, read2, read3):
                for j in i:
                    writer.writerow(j)

def filter_data():
    merge_csv_files('data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv')
    with open('merged.csv', 'r') as read:
        read = csv.reader(read, delimiter=',')
        next(read)
        with open('formated.csv', 'w') as file2:
            writer2 = csv.writer(file2)
            writer2.writerow(['Sales', 'Date', 'Region'])
            for i in read:
                sales = float(i[1].strip('$')) * int(i[2])
                date = i[3]
                region = i[4]
                writer2.writerow([sales, date, region])

    os.remove('merged.csv')

filter_data()