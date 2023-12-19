# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста
from flask import Flask, render_template, request


app = Flask(__name__)

@app.get('/')
def index():
    return render_template('form6.html')

@app.post('/')
def index_post():
    name = request.form.get('name')
    age = request.form.get('age')

    if int(age) >= 18:
        return render_template('name.html',context=name)
    else:
        return render_template('age18.html',context=name)


if __name__ == '__main__':
    app.run(debug=True)