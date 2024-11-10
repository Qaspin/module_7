def custom_write(file_name: str, strings: list):
    dict = {}
    line_number = 1
    file = open(file_name, 'w')
    for string in strings:
        line_byte = file.tell()
        file.write(f'{string}\n')
        dict[(line_number, line_byte)] = string
        line_number += 1
    file.close()
    return dict


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)