from pymongo import MongoClient
from parser import parse


def main():
    try:
        print('Подключаемся к базе данных...')
        client = MongoClient('mongodb://localhost:27017/')
        db = client['test']
        collection = db['news']
        print('Подключение прошло успешно!')
        print('')
    except Exception as Error:
        print(f"Произошла ошибка: {Error=}")
        return

    print('Парсинг начинается с первой страницы сайта РИАЦ раздела "Новости".')
    pages_count = int(input('Введите количество страниц, которое вы хотите распарсить: '))
    news = parse(pages_count)

    for new in news:
        link = new['link']
        try:
            collection.insert_one(new)
        except Exception:
            print(f'Новость "{link}" в базе уже есть!')


main()
