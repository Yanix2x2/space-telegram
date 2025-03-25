import requests
import os
from dotenv import load_dotenv

from datetime import datetime


def get_hubble_image(directory):
    image_name = 'hubble.jpeg'
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

    response = requests.get(url)
    response.raise_for_status()

    path = os.path.join(directory, image_name)
    with open(path, 'wb') as image:
        image.write(response.content)


def get_links_spacex_images():
    launch_id = '5eb87d47ffd86e000604b38a'
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
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


def get_links_nasa_images(api_key):
    params = {'api_key': api_key, 'count': 30}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    response.raise_for_status()
    links_nasa = []
    for link in response.json():
        links_nasa.append(link['url'])
    return links_nasa


def get_file_extension(link):
    file_extension = os.path.splitext(link)[-1]
    return file_extension


def fetch_nasa_apod(links_nasa, directory):
    for i, link in enumerate(links_nasa):
        response = requests.get(link)
        response.raise_for_status()
        file_extension = get_file_extension(link)
        image_name = f'nasa_apod_{i}{file_extension}'
        path = os.path.join(directory, image_name)
        with open(path, 'wb') as image:
            image.write(response.content)


def get_date(datestring):
    dt = datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')
    return dt.strftime("%Y/%m/%d")


def get_links_epic_images(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {'api_key': api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()

    links_epic = []
    for response in response.json():
        date = get_date(response['date'])
        filename = f'{response['image']}.png'
        link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{filename}'
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
    get_hubble_image(directory)

    links_spacex = get_links_spacex_images()
    fetch_spacex_last_launch(links_spacex, directory)

    links_nasa = get_links_nasa_images(api_key)
    fetch_nasa_apod(links_nasa, directory)

    links_epic = get_links_epic_images(api_key)
    fetch_epic_archive(links_epic, directory, api_key)


if __name__ == '__main__':
    main()
