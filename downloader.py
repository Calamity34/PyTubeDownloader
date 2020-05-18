import pytube
import os
import requests
from bs4 import BeautifulSoup as bs
import sys
from time import sleep

def get_video_info(url):
    # download HTML code
    content = requests.get(url)
    # create beautiful soup object to parse HTML
    soup = bs(content.content, "html.parser")
    # initialize the result
    result = {}
    # video title
    result['title'] = soup.find("span", attrs={"class": "watch-title"}).text.strip()
    return result['title']

video = input('Video URL: ')
title = get_video_info(video)
abort = input(f'Are you sure you want to download "{title}"? [Y/n]')
if abort != "":
    print('Exiting...')
    sys.exit()
else:
    print(f"Download path: {os.getcwd()} (Ctrl+C to abort)")
    sleep(1.5)
    print('Downloading...')
    path = ""
    pytube.YouTube(video).streams.first().download(path)
