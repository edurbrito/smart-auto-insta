from pykeyboard import PyKeyboard
import time
import pyperclip

def fileManager(photopath):
    pyperclip.copy(photopath)
    k = PyKeyboard()

    time.sleep(1)
    k.press_key(k.control_key) #autoit.win_active("Open") #open can change by your os language if not open change that
    k.tap_key("l")
    k.release_key(k.alt_key)
    time.sleep(1)
    k.press_key(k.control_key) #autoit.control_send("Open", "Edit1", photopath)
    k.tap_key("v")
    k.release_key(k.control_key)
    time.sleep(1)
    k.tap_key(k.enter_key) #autoit.control_send("Open", "Edit1", "{ENTER}")

def textToClipboard(text):
    pyperclip.copy(text)