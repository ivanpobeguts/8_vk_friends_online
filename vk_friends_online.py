import vk
import getpass
import argparse

APP_ID = 6607153


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


def get_online_friends(login, password, api_version=' 5.78'):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends',
        )
        api = vk.API(session, v=api_version)
        friends_online_ids = api.friends.getOnline()
        return api.users.get(user_ids=friends_online_ids)
    except vk.exceptions.VkAuthError:
        return None


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print(friend['first_name'], friend['last_name'])


if __name__ == '__main__':
    login = get_args().login
    password = get_user_password()
    if login and password:
        friends_online = get_online_friends(login, password)
        if friends_online is not None:
            output_friends_to_console(friends_online)
        else:
            print('Incorrect login or password')
    else:
        print('Please enter your password')
