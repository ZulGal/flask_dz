# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.
from flask import Flask, render_template, request
import math


app = Flask(__name__)

@app.get('/')
def index():
    return render_template('form7.html')

@app.post('/')
def index_post():
    number = int(request.form.get('number'))
    print(number)
    text = f'Квадратный корень {number}: {math.sqrt(number)}'
    print(text)
    return render_template('result7.html',text = text)


if __name__ == '__main__':
    app.run(debug=True)