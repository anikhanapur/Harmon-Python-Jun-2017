products = []
products.append({'id' : 5, 'name' : 'Pen', 'cost' : 60, 'units' : 40, 'category' : 'stationary'})
products.append({'id' : 9, 'name' : 'Hen', 'cost' : 70, 'units' : 20, 'category' : 'grocery'})
products.append({'id' : 4, 'name' : 'Ten', 'cost' : 30, 'units' : 90, 'category' : 'stationary'})
products.append({'id' : 6, 'name' : 'Den', 'cost' : 90, 'units' : 60, 'category' : 'grocery'})
products.append({'id' : 2, 'name' : 'Zen', 'cost' : 50, 'units' : 30, 'category' : 'stationary'})


def print_line():
    print('-' * 80)


def print_list(list):
    for item in list:
        print(item)
    print_line()


def sort(list, key):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if (list[i][key] > list[j][key]):
                [list[i], list[j]] = [list[j], list[i]]


print('default list :')
print_list(products)

print('Sorting by Id')
sort(products, 'id')
print_list(products)

print('Sorting by cost')
sort(products, 'cost')
print_list(products)


def sort_comparer(list, comparer):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            compare_result = comparer(list[i], list[j])
            if (compare_result > 0):
                [list[i], list[j]] = [list[j], list[i]]


def product_comparer_by_value(p1, p2):
    p1_value = p1['cost'] * p1['units']
    p2_value = p2['cost'] * p2['units']
    if (p1_value < p2_value):
        return -1
    if (p1_value == p2_value):
        return 0
    return 1


print('Sorting by product value [ cost * units] ')
sort_comparer(products, product_comparer_by_value)
print_list(products)


def get_descending_comparer(comparer):
    def descending_comparer(p1, p2):
        return comparer(p1, p2) * -1

    return descending_comparer


# def product_comparer_by_value_descending(p1, p2):
#     return product_comparer_by_value(p1, p2) * -1


product_comparer_by_value_descending = get_descending_comparer(product_comparer_by_value)


print('Sorting by product value [ cost * units] descending')
sort_comparer(products, product_comparer_by_value_descending)
print_list(products)


def filter_stationary():
    result = []
    for product in products:
        if (product['category'] == 'stationary'):
            result.append(product)

    return result


print('Stationary products')
stationary_products = filter_stationary()
print_list(stationary_products)


def filter(list, predicate):
    result = []
    for item in list:
        if (predicate(item)):
            result.append(item)

    return result


def costly_product_predicate(product):
    return product['cost'] >= 60


print('Costly Products [ cost >= 60 ]')
# costly_products = filter(products, costly_product_predicate)
costly_products = filter(products, lambda product: product['cost'] >= 60)
print_list(costly_products)


# def affordable_product_predicate(product):
#     # return product['cost'] < 60
#     return not costly_product_predicate(product)

# def negate(predicate):
#     def negated_predicate(item):
#         return not predicate(item)
#     return negated_predicate

negate = lambda fn: lambda item: not fn(item)

affordable_product_predicate = negate(costly_product_predicate)

print('Affordable Products [ cost < 60 ]')
affordable_products = filter(products, affordable_product_predicate)
print_list(affordable_products)


def get_or_predicate(predicate1, predicate2):
    def or_predicate(item):
        return predicate1(item) or predicate2(item)
    return or_predicate


affordable_or_grocery_product_predicate = get_or_predicate(affordable_product_predicate, lambda product : product['category'] == 'grocery')
affordable_or_grocery_products = filter(products, affordable_or_grocery_product_predicate)
print('Affordable OR grocery products')
print_list(affordable_or_grocery_products)


def group_by(list, key_selector):
    result = {}
    for item in list:
        key = key_selector(item)
        if (key not in result):
            result[key] = []
        result[key].append(item)
    return result


products_by_category = group_by(products, lambda product : product['category'])
print('Products by category')
print(products_by_category)
print_line()


def get_key_by_cost(product):
    if (product['cost'] >= 60):
        return 'costly'
    return 'affordable'


products_by_cost = group_by(products, get_key_by_cost)
print('Products by cost')
print(products_by_cost)
print_line()



