from os import popen


def update():
    res = popen(f'poetry run alembic upgrade head')
    print(res.read())


if __name__ == '__main__':
    update()
