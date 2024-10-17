import sys
from enum import Enum

from commands.user_management import register, login


class Commands(Enum):
    REGISTER = 'register'
    LOGIN = 'login'


def main():
    if Commands.REGISTER.value in sys.argv:
        register()
        sys.exit(0)
    if Commands.LOGIN.value in sys.argv:
        login()
        sys.exit(0)


if __name__ == '__main__':
    main()
