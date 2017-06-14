products = []
products.append({'id' : 5, 'name' : 'Pen', 'cost' : 60, 'units' : 40, 'category' : 'stationary'})
products.append({'id' : 9, 'name' : 'Hen', 'cost' : 70, 'units' : 20, 'category' : 'stationary'})
products.append({'id' : 4, 'name' : 'Ten', 'cost' : 30, 'units' : 90, 'category' : 'stationary'})
products.append({'id' : 6, 'name' : 'Den', 'cost' : 90, 'units' : 60, 'category' : 'stationary'})
products.append({'id' : 2, 'name' : 'Zen', 'cost' : 50, 'units' : 30, 'category' : 'stationary'})


def print_list(list):
    for item in list:
        print(item)


def sort():
    for i in range(5):
        for j in range(i + 1, 5):
            if (products[i]['id'] > products[j]['id']):
                [products[i], products[j]] = [products[j], products[i]]


print('default list :')
print_list(products)

print('Sorting')
sort()
print_list(products)
