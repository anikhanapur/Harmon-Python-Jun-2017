import csv


def csv_dict_reader(file_obj):

    reader = csv.DictReader(file_obj)
    result = [line for line in reader]
    return result


if __name__ == '__main__':
    with open('products.csv', 'r') as file_obj:
        result = csv_dict_reader(file_obj)
        print(result)


