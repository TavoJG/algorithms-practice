from datetime import datetime
from time import sleep


def time_count(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        func(*args, **kwargs)
        end_time = datetime.now()
        print(
            f'Execution time: {(end_time-start_time).microseconds} microseconds')
    return wrapper


if __name__ == '__main__':
    @time_count
    def counter():
        sleep(3)
        print('Hello')

    counter()
