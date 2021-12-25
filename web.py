from flask import Flask, render_template
from pymongo import MongoClient

# Flask приложение
app = Flask(__name__)

# Подключение к БД
client = MongoClient('mongodb://localhost:27017/')
db = client['test']
collection = db['news']

# Создание списка новостей
articles = []
for doc in collection.find():
    articles.append(doc)

# Отображение списка в браузере
@app.route('/')
def index():
    return render_template('index.html', articles=articles)


if __name__ == "__main__":
    app.run(debug=True)
