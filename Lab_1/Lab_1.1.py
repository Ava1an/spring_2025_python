numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
valid_numbers = [num for num in numbers if num is not None]

if not valid_numbers:
    result = numbers
else:
    average = sum(valid_numbers) / len(numbers)
    result = [average if num is None else num for num in numbers]

print("Измененный список:", result)



# TODO Найдите количество книг, которое можно разместить на дискете
v_disk = 1.44 * 1024 **2
lot_pages_in_book = 100
line_on_page = 50
symbols_on_line = 25
symbole_byte = 4

one_book = symbole_byte * symbols_on_line * line_on_page * lot_pages_in_book
ahahahah = v_disk // one_book

print("Количество книг, помещающихся на дискету:", int(ahahahah))






list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)
