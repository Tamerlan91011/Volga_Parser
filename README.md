## 🌐 Web приложение для парсинга с новостного сайта Волгоградской области

Целевой сайт для парсинга: https://riac34.ru/

ОС: *Linux (Ubuntu 18.04)* 

ЯП: *Python (3.7+)*

СУБД: *MongoDB*

Работали: *Глазунов Тимур, Аль Газали Муххамад*

## **Цель**: разработать программное приложение для парсинга новостного сайта Волгоградской области
## **Задача**:
Разработать [краулер](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA%D0%BE%D0%B2%D1%8B%D0%B9_%D1%80%D0%BE%D0%B1%D0%BE%D1%82), который будет собирать и сохранять в общую базу данных [MongoDB](https://www.mongodb.com/) следующие поля: 
- Название новости
- Дата новости
- Ссылка на новость
- Текст новости
- Ссылка на видео (если есть)
- Количество просмотров новости (если есть)
- Количество комментариев новости (если есть)

## **Что нужно установить:** ##
Python последней версии:

- `sudo apt-get install python3`

Python пакеты **requests** и **beautifulsoup** для работы с HTTP запросами на сайтах, и для обработки их контента:

- `pip install requests`

- `pip install beautifulsoup4`

Пакет для работы с MongoDB на языке Python

- `pip install pymongo`

- [Инструкция по установке MongoDB на Linux](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

Flask - фреймворк для создания веб-приложений на Python. Его будет достаточно для базового отображения результатов парсинга:

- `pip install Flask`


## **Как с этим работать** ##
Чтобы распарсить новостную ленту в **локальную** базу данных MongoDB, необходимо запустить парсер в соответствующей директории:
- `cd Volga_Parser/parser`
- `python3 main.py` 

Программа попросит ввести количество страниц, которое необходимо распарсить с сайта РИАЦ.
При успешном запуске будет выведено количество страниц, и количество полученных новостей.
Если новость в базе уже имеется, то будет выведено соответсвующее сообщение. 

Далее, чтобы посмотреть полученные новости в базе в виде веб-страницы, необходимо запустить Flask приложение в основной директории:
- `cd Volga_Parser`
- `python3 web.py`
