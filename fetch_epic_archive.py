import os
import requests
from dotenv import load_dotenv
from datetime import datetime
from urllib.parse import urljoin


BASE_URL = 'https://api.nasa.gov/EPIC/api/natural'


def get_links_epic_images(api_key):
    params = {'api_key': api_key}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    links_epic = []
    archive_url = urljoin(BASE_URL, '../archive/natural/')
    for response in response.json():
        date = (
            datetime
            .strptime(response['date'], '%Y-%m-%d %H:%M:%S')
            .strftime("%Y/%m/%d")
        )
        filename = f'{response['image']}.png'
        link = urljoin(archive_url, f'{date}/png/{filename}')
        links_epic.append(link)
    return links_epic


def fetch_epic_archive(links_epic, directory, api_key):
    params = {'api_key': api_key}
    for i, link in enumerate(links_epic):
        response = requests.get(link, params=params)
        response.raise_for_status()
        image_name = f'epic_archive_{i}.png'
        path = os.path.join(directory, image_name)
        with open(path, 'wb') as image:
            image.write(response.content)


def main():
    load_dotenv()
    api_key = os.environ["NASA_API_KEY"]
    directory = 'images'
    os.makedirs(directory, exist_ok=True)

    links_epic = get_links_epic_images(api_key)
    fetch_epic_archive(links_epic, directory, api_key)


if __name__ == '__main__':
    main()
