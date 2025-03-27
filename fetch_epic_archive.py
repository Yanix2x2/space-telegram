import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import urljoin
import argparse

from helper import save_pictures


BASE_URL = 'https://api.nasa.gov/EPIC/api/natural'


def get_epic_links(api_key):
    params = {'api_key': api_key}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    epic_links = []
    archive_url = urljoin(BASE_URL, '../archive/natural/')
    for response in response.json():
        date = (
            datetime
            .strptime(response['date'], '%Y-%m-%d %H:%M:%S')
            .strftime("%Y/%m/%d")
        )
        filename = f'{response['image']}.png'
        link = urljoin(archive_url, f'{date}/png/{filename}')
        epic_links.append(link)
    return epic_links


def fetch_epic_archive(epic_links, directory, api_key):
    params = {'api_key': api_key}
    for i, link in enumerate(epic_links):
        image_name = f'epic_archive_{i}.png'
        save_pictures(link, directory, image_name, params=params)


def main():
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]

    parser = argparse.ArgumentParser(description='Загрузка фотографий с Nasa')
    parser.add_argument('--directory', '-d', help='Директория для фото', default='images/epic')
    args = parser.parse_args()

    os.makedirs(args.directory, exist_ok=True)
    epic_links = get_epic_links(api_key)
    fetch_epic_archive(epic_links, args.directory, api_key)


if __name__ == '__main__':
    main()
