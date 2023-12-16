# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости,
# краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через
# контекст.
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    context = [
        {'header': 'Заголовок1',
         'description': 'Краткое описание1',
         'date': '2023.02.24' },
        {'header': 'Заголовок2',
         'description': 'Краткое описание2',
         'date': '2022.03.29'},
    ]
    return render_template('index.html', context=context)


if __name__ == "__main__":
    app.run(debug=True)
