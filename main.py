import requests
import os

IMAGES_DIR = 'images/'

def define_extension(image_url):
    return '.'+image_url.split('.')[-1]


def get_image_from_url(url, filename):
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)
    response = requests.get(url)
    if response.ok:
        with open(filename, 'wb') as file:
            file.write(response.content)


def download_images(image_url, image_name):
    print('Сохраняем картинку {}'.format(image_url))
    get_image_from_url(image_url, IMAGES_DIR+image_name+define_extension(image_url))
    print('Картинка сохранена')    


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')
    images =response.json()['links']['flickr_images']
    for image_number, image in enumerate(images):
        download_images(image, 'spacex'+str(image_number+1))


def fetch_hubble_image(image_id):
    hubble_url = 'http://hubblesite.org/api/v3/image/'+str(image_id)
    response = requests.get(hubble_url)
    if response.ok:
        hubble_images = response.json()['image_files']
        images = [image['file_url'] for image in hubble_images]
        download_images(images[-1], 'hubble_'+str(image_id))


if __name__ == '__main__':

    fetch_spacex_last_launch()
    fetch_hubble_image(1)
