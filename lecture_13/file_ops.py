with open('example2.txt', 'w+', encoding='utf-8') as file:
    file.write('Hello, world!\n')


with open('img.png', 'rb') as cat:
    content = cat.read()
    print(content)
    with open('cat.png', 'wb') as copy_cat:
        copy_cat.write(content)



