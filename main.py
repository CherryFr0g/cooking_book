import sys
from enum import Enum

from commands.receipt_management import create_receipt
from commands.user_management import register, login


class Commands(Enum):
    REGISTER = "register"
    LOGIN = "login"
    HELP = "help"
    CREATE_RECEIPT = "create_receipt"


command_descriptions = {
    Commands.REGISTER.value: "Команда регистрации",
    Commands.LOGIN.value: "Команда для входа",
    Commands.HELP.value: "Вызов справки",
    Commands.CREATE_RECEIPT.value: "Создание нового рецепта"
}


def show_help():
    print("Все доступные команды: \n")
    for k, v in command_descriptions.items():
        print(f"\t{k}: {v}")


command_callbacks = {
    Commands.REGISTER.value: register,
    Commands.LOGIN.value: login,
    Commands.HELP.value: show_help,
    Commands.CREATE_RECEIPT.value: create_receipt,
}


def main():
    if len(sys.argv) > 0 and sys.argv[1] in command_callbacks:
        command_callbacks[sys.argv[1]]()
        sys.exit(0)
    else:
        print("На данный момент такой команды не существует, но мы обязательно ее добавим \n"
              "Для получения актуального списка команд наберите в консоли -python main.py help")


if __name__ == '__main__':
    main()
