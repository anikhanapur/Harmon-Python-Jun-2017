import csv


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        print(row)


if __name__ == '__main__':
    file_name = 'products.csv'
    with open(file_name, 'r') as file_obj:
        csv_reader(file_obj)

