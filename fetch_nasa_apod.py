import os
import requests
from dotenv import load_dotenv

from helper import get_file_extension


def get_links_nasa_images(api_key):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key, 'count': 5}
    response = requests.get(url, params=params)
    response.raise_for_status()
    links_nasa = []
    for link in response.json():
        links_nasa.append(link.get('url'))
    return links_nasa


def fetch_nasa_apod(links_nasa, directory):
    for i, link in enumerate(links_nasa):
        if not link:
            continue
        response = requests.get(link)
        response.raise_for_status()
        file_extension = get_file_extension(link)
        image_name = f'nasa_apod_{i}{file_extension}'
        path = os.path.join(directory, image_name)
        with open(path, 'wb') as image:
            image.write(response.content)


def main():
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    directory = 'images/nasa' 
    os.makedirs(directory, exist_ok=True)

    links_nasa = get_links_nasa_images(api_key)
    fetch_nasa_apod(links_nasa, directory)


if __name__ == '__main__':
    main()