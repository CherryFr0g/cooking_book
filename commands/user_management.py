from sqlalchemy.orm import Session

from database import engine, User


def register():
    print("Добро пожаловать, пройдите быструю регистрацию.")
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    middle_name = input('Отчество (при наличии): ')

    with Session(engine) as session:
        try:
            user = User(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
            )
            session.add(user)
            session.commit()
            print(f" Приветствуем {first_name}, Ваш id: {user.id}")
        except Exception:
            print("Не удалось зарегистрироваться, попробуйте снова")


def login():
    id_login = input("Введите Ваш id: ")

    with Session(engine) as session:
        if user := session.query(User).filter_by(id=id_login).first():
            print(f"Добро пожаловать {user.first_name}")
        else:
            print("Такого пользователя не существует")
            answer = input("Желаете пройти быструю регистрацию? [Д/Н] ")
            if answer.lower() == "д":
                register()
                login()
            else:
                print("Жаль! Приходите еще")

