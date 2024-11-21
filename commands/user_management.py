from pydantic import ValidationError
from sqlalchemy.orm import Session

from database import engine, User
from models.user import UserModel, LoginModel

def register():
    print("Добро пожаловать, пройдите быструю регистрацию.")
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    middle_name = input('Отчество (при наличии): ')

    with Session(engine) as session:
        try:
            user_data = UserModel(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
            )
            user = User(**user_data.model_dump(exclude_unset=True))
            session.add(user)
            session.commit()
            print(f" Приветствуем {first_name}, Ваш id: {user.id}")

        except ValidationError as err:
            print(f"Вы ввели неверные данные {err=}")

        except Exception:
            print("Не удалось зарегистрироваться, попробуйте снова")


def login():
    id_login = input("Введите Ваш id: ")
    try:
        user_id = LoginModel(id=id_login).id
    except:
        print("ID должен состоять только из чисел")
        return


    with Session(engine) as session:
        if user := session.query(User).filter_by(id=user_id).first():
            print(f"Добро пожаловать {user.first_name}")
        else:
            print("Такого пользователя не существует")
            answer = input("Желаете пройти быструю регистрацию? [Д/Н] ")
            if answer.lower() == "д":
                register()
                login()
            else:
                print("Жаль! Приходите еще")

