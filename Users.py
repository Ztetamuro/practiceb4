import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import find_athletes as fa

SQLITE_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
    """
    Описывает структуру таблицы user, содержащую данные пользователя
    """
    __tablename__ = "user"
    id = sa.Column(sa.INTEGER, primary_key = True, autoincrement = True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.FLOAT)

class Athelete(Base):
    """
    Описывает структуру таблицы athelete, содержащую данные пользователя
    """
    __tablename__ = "athelete"
    id = sa.Column(sa.INTEGER, primary_key = True, autoincrement = True)
    name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.FLOAT)

def db_connect():
    """
    Создает подключение к базе данных
    """
    engine = sa.create_engine(SQLITE_PATH)
    session = sessionmaker(engine)
    return session()

def add_user():
    """
    Запрашивает у пользователя данные для последующего внесения в базу данных
    """
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    gender = input("Введите пол(Male - мужской, Female - женский): ")
    email = input("Укажите адресс электронной почты: ")
    birthdate = input("Укажите дату рождения в формате год-месяц-день (например: 1970-01-13): ")
    height = input("Укажите рост в метрах и сантиметрах через точку(например: 1.87): ")

    user = User(
        first_name = first_name,
        last_name = last_name,
        gender = gender,
        email = email,
        birthdate = birthdate,
        height = height
    )
    return user

def main():
    """
    Создает метод коммуникации пользователя с базой данных
    """
    session = db_connect()
    request = input("Приветик!\n"
          "Выберите действие, которое хотите совершить:\n"
          "1 - добавить нового пользователя\n"
          "2 - найти по id пользователя с похожими параметрами роста и дня рождения\n")
    if request == "1":
        user = add_user()
        session.add(user)
        session.commit()
        print("Пользователь добавлен")
    elif request == "2":
        user_id = input("Введите ID пользователя для поиска схожих данных с спорцменами: ")
        coincidence, coincidence1, usr_data, usr_data_1 = fa.find_by_id(user_id, session)
        print("{}\n{}\n{}\n{}".format(usr_data, usr_data_1, coincidence, coincidence1))
    else:
        print("Выбрана несуществующая команда")

if __name__ in "__main__":
    main()