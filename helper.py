import os
from urllib.parse import urlparse


def get_file_extension(link):
    parsed = urlparse(link)
    path = parsed.path
    filename = os.path.basename(path)
    extension = os.path.splitext(filename)[1]

    return extension.lower()
