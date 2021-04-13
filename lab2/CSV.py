import random
import string

table_names = ['group', 'subgroup', 'seller', 'product', 'cart', 'customer', 'payment']
group_names = [
    'Electronics', 'Computers', 'Smart Home', 'Beauty'
]
subgroup_names = [
    'Camera', 'Monitors', 'Plugs', 'Makeup'
]
product_names = [
    'GoPro', 'ZOWIE_XL2546', 'Wemo', 'Cream'
]
card_types = [
    'MasterCard', "Visa"
]
names = [
    'Mark', 'Amber', 'Todd', 'Anita', 'Sandy',
    'John', 'Fred', 'Jason', 'Keyser', 'Lily',
    'Anna', 'Mike', 'Luke', 'Andrea', 'Lisa',
    'Stephen', 'James', 'Albert', 'Emma', 'Lia',
]


def generate_random_csv(filename='generated_data.csv', entries=250):
    group_columns = 'id,name\n'
    data_list = []
    for id in range(1, len(group_names) + 1):
        name = group_names[id - 1]
        data_list.append(','.join([str(id), name]) + '\n')
    with open(filename, 'w') as file:
        file.write('group\n')
        file.write(group_columns)
        file.writelines(data_list)

    subgroup_columns = 'id,name,group_id\n'
    data_list = []
    for id in range(1, len(subgroup_names) + 1):
        name = subgroup_names[id - 1]
        group_id = id
        data_list.append(','.join([str(id), name, str(group_id)]) + '\n')
    with open(filename, 'a') as file:
        file.write('subgroup\n')
        file.write(subgroup_columns)
        file.writelines(data_list)

    seller_columns = 'id,name\n'
    data_list = []
    for id in range(1, entries + 1):
        name = random.choice(names)
        data_list.append(','.join([str(id), name]) + '\n')
    with open(filename, 'a') as file:
        file.write('seller\n')
        file.write(seller_columns)
        file.writelines(data_list)

    product_columns = 'id,name,subgroup_id,seller_id, cart_id\n'
    data_list = []
    for id in range(1, entries + 1):
        name = random.choice(product_names)
        subgroup_id = product_names.index(name) + 1
        seller_id = id
        cart_id = ''
        data_list.append(','.join([str(id), name, str(subgroup_id), str(seller_id), cart_id]) + '\n')
    with open(filename, 'a') as file:
        file.write('product\n')
        file.write(product_columns)
        file.writelines(data_list)

    cart_columns = 'id,number_of_products,total\n'
    data_list = []
    for id in range(1, entries + 1):
        number_of_products = '0'
        total = '0'
        data_list.append(','.join([str(id), number_of_products, total]) + '\n')
    with open(filename, 'a') as file:
        file.write('cart\n')
        file.write(cart_columns)
        file.writelines(data_list)

    customer_columns = 'id,name,address,phone_number,cart_id\n'
    data_list = []
    for id in range(1, entries + 1):
        name = random.choice(names)
        address = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 12))).title()
        phone = ''.join(random.choices(string.digits, k=8))
        cart_id = id
        data_list.append(','.join([str(id), name, address, phone, str(cart_id)]) + '\n')
    with open(filename, 'a') as file:
        file.write('customer\n')
        file.write(customer_columns)
        file.writelines(data_list)


    payment_columns = 'id,customer_id,card_type,card_number\n'
    data_list = []
    for id in range(1, entries + 1):
        card_type = random.choice(card_types)
        card_number = ''.join(random.choices(string.digits, k=16))
        data_list.append(','.join([str(id), str(id), card_type, card_number]) + '\n')
    with open(filename, 'a') as file:
        file.write('payment\n')
        file.write(payment_columns)
        file.writelines(data_list)


def parse_csv(filename='generated_data.csv'):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line[:-1] for line in lines if line.endswith('\n')]

    tables = []
    columns = []
    data = []
    for table in table_names:
        tables.append(lines.index(table))
    for index in range(len(tables) - 1):
        columns.append(lines[tables[index] + 1])
        data.append(lines[tables[index] + 2 : tables[index + 1]])
    columns.append(lines[tables[len(tables) - 1] + 1])
    data.append(lines[tables[len(tables) - 1] + 2:])

    return {
        'group': (columns[0], data[0]),
        'subgroup': (columns[1], data[1]),
        'seller': (columns[2], data[2]),
        'product': (columns[3], data[3]),
        'cart': (columns[4], data[4]),
        'customer': (columns[5], data[5]),
        'payment': (columns[6], data[6])
    }

if __name__ == '__main__':
    generate_random_csv()
    # output = parse_csv()
    # print(str(output))