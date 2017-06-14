import csv


def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    header = None
    result = []
    for row in reader:
        if not header:
            header = row
        else:
            item = {}
            for index in range(len(row)):
                attr_name = header[index]
                attr_value = row[index]
                item[attr_name] = attr_value
            result.append(item)
    return result


if __name__ == '__main__':
    file_name = 'products.csv'
    with open(file_name, 'r') as file_obj:
        items = csv_reader(file_obj)
        print(items)

