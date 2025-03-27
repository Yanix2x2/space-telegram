import os
import requests
from dotenv import load_dotenv
import argparse

from helper import get_file_extension, save_pictures


def get_nasa_links(api_key, count):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key, 'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    nasa_links = [link.get('url') for link in response.json()]
    return nasa_links


def fetch_nasa_apod(nasa_links, directory):
    for i, link in enumerate(nasa_links):
        if not link:
            continue
        file_extension = get_file_extension(link)
        image_name = f'nasa_apod_{i}{file_extension}'
        save_pictures(link, directory, image_name)


def main():
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    
    parser = argparse.ArgumentParser(description='Загрузка фотографий с Nasa')
    parser.add_argument('--directory', '-d', help='Директория для фото', default='images/nasa')
    parser.add_argument('--count', '-c', help='Сколько скачать фото', default='30')
    args = parser.parse_args()

    os.makedirs(args.directory, exist_ok=True)
    nasa_links = get_nasa_links(api_key, args.count)
    fetch_nasa_apod(nasa_links, args.directory)


if __name__ == '__main__':
    main()
