import os

# 讀取檔案
def read_file(filename):
    products = []	
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    print(products)
    return products

# 使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入價格: ')
        price = int(price)
        products.append([name, price])
    print(products)
    return products

# 列印購買紀錄
def print_product(products):
    for p in products:
        print(f'商品: {p[0]}, 價格: {p[1]}')

# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('file is found')
        products = read_file(filename)
    else:
       print('file is not found')

    products = user_input(products)
    print_product(products)
    write_file(filename, products)

if __name__ == '__main__':
    main()
