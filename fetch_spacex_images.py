import os
import requests
import argparse
from urllib.parse import urljoin

BASE_URL = 'https://api.spacexdata.com/v5/launches/'


def get_links_spacex_images():
    parser = argparse.ArgumentParser(
        description='Загрузка фотографий с указанным id'
    )
    parser.add_argument('--launch_id', help='ID запуска', default='latest')
    args = parser.parse_args()
    url = urljoin(BASE_URL, args.launch_id)
    response = requests.get(url)
    response.raise_for_status()
    links_spacex = response.json()['links']['flickr']['original']
    return links_spacex


def fetch_spacex_last_launch(links_spacex, directory):
    for i, link in enumerate(links_spacex):
        response = requests.get(link)
        response.raise_for_status()

        image_name = f'spacex_{i}.jpg'
        path = os.path.join(directory, image_name)
        with open(path, 'wb') as image:
            image.write(response.content)


def main():
    directory = 'images'
    
    os.makedirs(directory, exist_ok=True)

    links_spacex = get_links_spacex_images()
    fetch_spacex_last_launch(links_spacex, directory)


if __name__ == '__main__':
    main()
