import sys
from time import sleep

def write_with_delay(string: str, delay: float):
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(delay)

def _test():
    write_with_delay('test', 1)

if __name__ == '__main__':  
    _test()
