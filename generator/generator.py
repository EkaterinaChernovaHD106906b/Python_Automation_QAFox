import random


def generated_file():
    path = rf'C:\Users\user\PycharmProjects\Python_Automation_QAFox\filetest{random.randint(0,100)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello World{random.randint(0, 100)}')
    file.close()
    return file.name, path
