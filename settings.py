import os


def history(url):
    if os.path.isfile('catch'+url):
        print("histry exists")
    else:
        print("no history exists")
    return True

