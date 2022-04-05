# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from __future__ import unicode_literals
import youtube_dl


def downlaod(url, path):
    print("URL is ", url)
    print("Path is ", path)

    ydl_opts = {
    'outtmpl': path+'%(title)s-%(id)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print("DONE :)")

def main():
    url = input("URL: ")
    path = input("Path: ")

    downlaod(url, path)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
