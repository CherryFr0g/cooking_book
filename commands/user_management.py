from sqlalchemy.orm import Session

from database import engine, User


def register():
    print("Добро пожвловать, пройдите быструю регистрацию.")
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
            print(f" Приветствуем {first_name}")
        except Exception:
            print("Не удалось зарегистрироваться, попробуйте снова")


