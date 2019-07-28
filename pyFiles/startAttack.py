from pyFiles.cloneURL import downloadHTML
import threading
import pyFiles.config as config
from FlaskWebserver import startWebserver

def startAttack():
    try:
        downloadHTML()
        config.serverIsUp = True
        threading.Thread(target=startWebserver).start()
    except Exception as e:
        print("An Error occured " + e)
