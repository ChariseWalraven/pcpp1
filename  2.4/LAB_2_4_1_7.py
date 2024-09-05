from datetime import  datetime
def log_timestamp(function):
    def inner(*args):
        dt = datetime.now()
        print(datetime.strftime(dt, '%Y-%m-%d %H:%M:%S'))
        function(*args)

    return inner

@log_timestamp
def add(a, b):
    print(a + b)

add(1,2)
