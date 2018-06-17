import vk
import getpass
import argparse


APP_ID = -1  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'login',
        help='vk login',
        type=str,
    )
    args = parser.parse_args()
    return args


def get_user_password():
    return getpass.getpass('Enter your password: ')


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
    )
    api = vk.API(session)
    # например, api.friends.get()


def output_friends_to_console(friends_online):
    pass

if __name__ == '__main__':
    login = get_args().login
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
