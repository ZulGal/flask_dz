# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".
from flask import Flask, flash, redirect, render_template,request, url_for


app = Flask(__name__)

app.secret_key =b'5d65e8d6267c8e1af137bec66a3f1c05cf019543e95b588a9152f0fa2aa65f14'

@app.route('/')
def index():
    return render_template('form_flash8.html')

@app.post('/form/')
def form():
    name = request.form.get('name')
    flash(f'Форма успешно отправлена!', 'success')
    return render_template('form_flash8.html', name=name)



if __name__ == '__main__':
    app.run(debug=True)

