# Задание №5
# 📌 Создать форму регистрации для пользователя.
# 📌 Форма должна содержать поля: имя, электронная почта,
# пароль (с подтверждением), дата рождения, согласие на
# обработку персональных данных.
# 📌 Валидация должна проверять, что все поля заполнены
# корректно (например, дата рождения должна быть в
# формате дд.мм.гггг).
# 📌 При успешной регистрации пользователь должен быть
# перенаправлен на страницу подтверждения регистрации.
from flask import Flask,render_template, request
from flask_wtf.csrf import CSRFProtect

from forms_5 import RegistrationForm
app = Flask(__name__)
app.config['SECRET_KEY'] = b'd101c7eb5025d86cccb03be884724e25e1a387e45a5e75de353e3e06baef0ab9'

from flask_dz.task3_5.models_5 import db, Regdata
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///regdata.sqlite'
db.init_app(app)

from werkzeug.security import generate_password_hash, check_password_hash

csrf = CSRFProtect(app)

@app.route('/register/', methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        birthday = form.birthday.data
        consent_personal = form.consent_personal.data
        db.create_all()
        print('Created DB!')
        regdata = Regdata(username=username, email=email,password=generate_password_hash(password),birthday=birthday,consent_personal=consent_personal)
        db.session.add(regdata)
        db.session.commit()
        print('DB filled')
    return render_template('register.html', form=form)

# @app.cli.command('init-db')
# def init_db():
#     db.create_all()
#     print('Created DB!')
#
# @app.cli.command('fill-db')
# def fill_db(regdata):
#     db.session.add(regdata)
#     db.session.commit()
#     print('DB filled')

# @app.cli.command("add-regdata")
# def add_user():
#     regdata = Regdata(username=username, email='john@example.com')
#     db.session.add(regdata)
#     db.session.commit()
# print('John add in DB!')

if __name__=='__main__':
    app.run(debug=True)
