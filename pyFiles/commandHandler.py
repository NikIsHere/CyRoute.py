import requests
from pyFiles import config
import validators
from pyFiles.startAttack import startAttack
import pickle
import time
from pyFiles.cloneURL import downloadHTML

help_text = open("help.txt", "r")
help_content = help_text.read()


def Handler():

    try:
        config.url, config.port = pickle.load(open("var.cfg", "rb"))
        print("Config file was loaded successfully")
    except Exception as e:
        print("Warning! If config was saved file is missing!")

    try:
        print("###  PRESS CTRL + C TO ESCAPE  ###")
        print("###  TYPE \"help\" FOR HELP  ###")

        while True:
            command = input(">>>")

            if command.lower() == "help":
                print(help_content)

            if command.lower() == "show":
                print("URL IS SET TO: \"{}\" , PORT IS SET TO {}".format(config.url, config.port))
                if config.serverIsUp:
                    print("Server should be running...")
                else:
                    print("Server seems to be offline...")

            if command.lower() == "set":
                try:
                    while True:
                        arg1 = input("OPTION >>> ")

                        if arg1.lower() == "url":
                            arg2 = input("VALUE >>> ")
                            if validators.url(arg2):
                                config.url = arg2
                            else:
                                print("PLEASE INPUT A VALID URL like \"http://www.google.de\"")

                        if arg1.lower() == "port":
                            arg2 = input("VALUE >>> ")
                            if arg2.isnumeric():
                                config.port = arg2
                            else:
                                print("PLEASE INPUT A VALID NUMERIC PORT")
                except KeyboardInterrupt:
                    print("Back to Main Menu")

            if command.lower() == "start":
                startAttack()
                time.sleep(1)
                print(">>> Attack started!")

            if command.lower() == "shutdown":
                config.serverIsUp = False
                print(requests.post("http://127.0.0.1:{}/shutdown".format(config.port)).text)

            if command.lower() == "save":
                print("Config is being saved for you!")
                pickle.dump([config.url, config.port], open("var.cfg", "wb"))

            if command.lower() == "download":
                downloadHTML()
                print("Downloaded site!")



    except KeyboardInterrupt:
        exit = input("Are you sure that you want to exit? (y/n)")

        if exit.lower() == "y":

            if config.serverIsUp:
                print(requests.post("http://127.0.0.1:{}/shutdown".format(config.port)).text)

        else:
            Handler()
