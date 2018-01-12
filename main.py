import time


def intro():
    print('Hey.')
    time.sleep(1)
    print('What is your name?')
    name = input()
    time.sleep(1)
    print('How are you ' + name + '?')
    status = input()
    time.sleep(1)


def talk():
    converse = input()
    if converse.find('?') == -1 and converse != None:
        print('Okay.')
        talk()
    else:
        print('Umm... Not sure.')
        talk()

if __name__ == '__main__':
    intro()
    print('Ok.')
    talk()