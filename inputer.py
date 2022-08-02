# from pymouse import * # Пакет, используемый моделируемой мышью
# from pykeyboard import * # Пакет, используемый имитацией клавиатуры

# mouse = PyMouse () # экземпляр мыши m
# key = pykeyboard () # экземпляр клавиатуры k
# from pymouse import PyMouse 
import time
from pykeyboard import PyKeyboard 
# m = PyMouse() 
key = PyKeyboard() 


# x_dim, y_dim = m.screen_size () m.click (x_dim // 2, y_dim // 2, 1) # округлить вниз до ближайшего целого числа k.type_string ('Hello, World!') 
while True:
    time.sleep(5)
    key.press_key('H') # which you then follow with a release of the key 
    key.release_key('H') # or you can 'tap' a key which does both 
    key.tap_key('e') # note that that tap_key does support a way of repeating keystrokes with a interval time between each 
    key.tap_key('l',n=2,interval=5) # and you can send a string if needed too 
    key.type_string('o World!') 


# key.type_string ('hello world') # имитировать строку ввода с клавиатуры
# key.press_key ("H") #- имитировать нажатие клавиши H с клавиатуры 
# key.release_key ("H") #- имитируйте клавиатуру, чтобы отпустить клавишу H. 
