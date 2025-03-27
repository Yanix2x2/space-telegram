import os
import requests
import argparse
from urllib.parse import urljoin

from helper import save_pictures

BASE_URL = 'https://api.spacexdata.com/v5/launches/'


def get_spacex_links(launch_id):
    url = urljoin(BASE_URL, launch_id)
    response = requests.get(url)
    response.raise_for_status()
    spacex_links = response.json()['links']['flickr']['original']
    return spacex_links


def fetch_spacex_last_launch(spacex_links, directory):
    for i, link in enumerate(spacex_links):
        image_name = f'spacex_{i}.jpg'
        save_pictures(link, directory, image_name)


def main():
    parser = argparse.ArgumentParser(
        description='Загрузка фотографий со SpaceX с указанным id запуска'
    )
    parser.add_argument('--launch_id', '-l', help='ID запуска', default='latest')
    parser.add_argument('--directory', '-d', help='Директория для фото', default='images/spacex')
    args = parser.parse_args()

    os.makedirs(args.directory, exist_ok=True)

    spacex_links = get_spacex_links(args.launch_id)
    fetch_spacex_last_launch(spacex_links, args.directory)


if __name__ == '__main__':
    main()
