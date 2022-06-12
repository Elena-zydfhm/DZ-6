# 1-  Написать программу вычисления арифметического выражения заданного строкой. 
# Используются операции +,-,/,*. приоритет операций стандартный. 
# Функцию eval не использовать! Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций. 
# Пример: 1+2*3 => 7; (1+2)*3 => 9;

# def calculate_operand(num1, operand, num2):
#   if operand == '*':
#     return float(num1) * float(num2)
#   if operand == '/':
#     return float(num1) / float(num2)
#   if operand == '+':
#     return float(num1) + float(num2)
#   if operand == '-':
#     return float(num1) - float(num2)


# def parse_expression(expression):
#   operation_list = ['+', '-', '/', '*']
#   numbers = expression
#   for operation in operation_list:
#     numbers = numbers.replace(operation, ' ')
#   numbers = numbers.split()
#   operations = []
#   for symbol in expression:
#     if not symbol.isdigit():
#       operations.append(symbol)

#   if expression[0] == '-':
#     numbers[0] = '-' + number[0]
#     del operations[0]

#   return numbers, operations


# def calculate_expression(numbers, operations):
#   operation_priority = ['*', '/', '-', "+"]
#   for _ in range(len(operations)):
#     for operand in operation_priority:
#       if operand in operations:
#         break
#     position = operations.index(operand)
#     result_of_operation = calculate_operand(numbers[position], operand, numbers[position+1])
#     del numbers[position+1]
#     del operations[position]
#     numbers[position] = str(result_of_operation)

#   return numbers



# expression = '12/4*3-2+11'
# numbers, operations = parse_expression(expression)
# result = calculate_expression(numbers, operations)
# print(result)


# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок 
# из какой-то книги, а втором файлике — сжатая версия этого текста). 
def encode_text(text):
  encoded_text = []
  count_of_repeat = 1
  for line in text:
    encoded_line = ''
    first_symb = line[0]
    second_symb = ''
    for symbol in line[1:]:
      second_symb = first_symb
      first_symb = symbol

      if second_symb == first_symb:
        count_of_repeat += 1

      else:
        encoded_line += str(count_of_repeat) + second_symb
        count_of_repeat = 1

    if first_symb != '\n':
      encoded_line += str(count_of_repeat) + first_symb

    encoded_text.append(encoded_line)
  return encoded_text


def decode_text(text):
  decoded_text = []
  for line in text:
    decoded_line = ''
    symbol = ''
    count_of_repeat = ''
    for symbol_position in range(len(line)):
      symbol = line[symbol_position]
      if symbol.isdigit():
        count_of_repeat += symbol
      else:
        decoded_line += symbol * int(count_of_repeat)
        count_of_repeat = ''

    decoded_text.append(decoded_line)
  return decoded_text


input_file = "The Captain's Daughter.txt"
output_file  = 'Decoded literary work.txt'

with open(input_file, 'r', encoding='utf-8') as read_file:
  text = read_file.readlines()
encoded_text = encode_text(text)

with open(output_file, 'w', encoding='utf-8') as write_file:
  for line in encoded_text:
    write_file.write(line + '\n')

decoded_text = decode_text(encoded_text)
print(decoded_text)


# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, 
# которая идет через 13 букв после нее в алфавите. ROT13 является примером шифра 
# Цезаря. Создайте функцию, которая принимает строку и возвращает строку, 
# зашифрованную с помощью Rot13 . Если в строку включены числа или специальные 
# символы, они должны быть возвращены как есть. Также создайте функцию, которая 
# расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.

# def encode_text(text):
#   encoded_text = ''
#   for symbol in text:
#     if symbol.isalpha():
#       encoded_text += chr(ord(symbol) + 13)
#     else:
#       encoded_text += symbol
#   return encoded_text


# def decode_text(text):
#   encoded_text = ''
#   for symbol in text:
#     if symbol.isalpha():
#       encoded_text += chr(ord(symbol) - 13)
#     else:
#       encoded_text += symbol
#   return encoded_text


# text = 'abclkergf;qeu oi;18p988`;khjkh ;h'
# encoded_text = encode_text(text)
# print(encoded_text)
# decoded_text = decode_text(encoded_text)
# print(decoded_text)