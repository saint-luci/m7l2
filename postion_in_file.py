def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, "w", encoding = "utf-8")
    for str_ in strings:
        file.write(f"{str(str_)}\n")
    file.close()
    file = open(file_name, "r", encoding = "utf-8")
    i = 0
    line = "\n"
    while True:
        key = [0]*2
        key[0] = i+1
        key[1] = file.tell()
        line = file.readline()
        if line == "":
            break
        string_positions[tuple(key)] = line[:-1]
        i += 1
    file.close()
    return string_positions
    
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
