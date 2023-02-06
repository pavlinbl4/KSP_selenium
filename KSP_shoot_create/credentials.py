from dotenv import load_dotenv
import os


def get_credintails():
    load_dotenv()
    login = os.environ.get('login')
    password = os.environ.get('password')
    first_loggin = os.environ.get('first_loggin')
    return login, password, first_loggin


if __name__ == '__main__':
    print(get_credintails())
