import os
from urllib.parse import urlparse

import requests


def get_file_extension(link):
    parsed = urlparse(link)
    path = parsed.path
    filename = os.path.basename(path)
    extension = os.path.splitext(filename)[1]

    return extension.lower()


def save_pictures(link, directory, image_name, params=None):
    response = requests.get(link, params=params)
    response.raise_for_status()
    path = os.path.join(directory, image_name)
    with open(path, 'wb') as image:
        image.write(response.content)


def directory_walk(directory):
    path = []
    for address, dirs, files in os.walk(directory):
        for file in files:
            path.append(os.path.join(address, file))
    return path
