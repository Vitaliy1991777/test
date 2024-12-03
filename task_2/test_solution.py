# import unittest
# import os
# from unittest.mock import patch, MagicMock
# from solution import parse_wiki_animals, save_to_csv

# class TestWikiAnimalsParser(unittest.TestCase):
#     @patch('solution.requests.get')
#     def test_parse_wiki_animals(self, mock_get):
#         # Мокируем ответ от Wikipedia
#         mock_response = MagicMock()
#         mock_response.status_code = 200
#         mock_response.text = '''<html><body><div class="mw-category-group"><ul><li><a href="/wiki/Животное_1">Животное 1</a></li></ul></div></body></html>'''
#         mock_get.return_value = mock_response
        
#         animal_counts = parse_wiki_animals()

#         # Проверка базовых условий
#         self.assertTrue(len(animal_counts) > 0)
#         self.assertTrue(all(letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ' for letter in animal_counts.keys()))
#         self.assertTrue(all(isinstance(count, int) and count >= 0 for count in animal_counts.values()))

#     def test_save_to_csv(self):
#         test_counts = {'А': 100, 'Б': 200, 'В': 150}
#         csv_filename = 'test_beasts.csv'
        
#         save_to_csv(test_counts, csv_filename)
        
#         # Проверка создания файла
#         self.assertTrue(os.path.exists(csv_filename))
        
#         # Проверка содержимого файла
#         with open(csv_filename, 'r', encoding='utf-8') as f:
#             lines = f.readlines()
        
#         self.assertEqual(len(lines), 3)
#         self.assertEqual(lines[0].strip(), 'А,100')
#         self.assertEqual(lines[1].strip(), 'Б,200')
#         self.assertEqual(lines[2].strip(), 'В,150')
        
#         # Удаляем тестовый файл
#         os.remove(csv_filename)

# if __name__ == '__main__':
#     unittest.main()

from solution import parse_wiki_animals, save_to_csv

# Пример теста
def test_parse_wiki_animals():
    base_url = "https://ru.wikipedia.org/w/index.php?title=Категория:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&from="
    letters = ['А', 'Б', 'В', 'Г', 'Д']
    
    # Вызов функции для парсинга данных
    data = parse_wiki_animals(base_url, letters)
    
    # Проверим, что данные не пустые
    assert len(data) > 0, "Данные пусты"
    
    # Проверим, что для каждой буквы есть результат
    for letter, count in data:
        assert isinstance(letter, str), f"Ожидался тип str для буквы, но получен {type(letter)}"
        assert isinstance(count, int), f"Ожидался тип int для количества, но получен {type(count)}"
    
    # Запишем в CSV
    save_to_csv(data)

# Запуск теста
test_parse_wiki_animals()


