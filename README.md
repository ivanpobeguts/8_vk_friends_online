# Watcher of Friends Online

The script uses vk API to get user's friends online.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# How to use

You should enter your login as a parameter and then type your password.
Example on Linux (for Windows the same):

```bash
$ python vk_friends_online.py login
Enter your password: 

Иван Иванов
Татьяна Володина
Сергей Петров
Анна Андреева
Владимир Ильин
...

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
