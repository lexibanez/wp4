import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO
import requests
import random
from datetime import datetime
from fileio import store_urls
from display_imgs import display_imgs

# API KEY
# YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY

# EXAMPLE URL
# https://api.nasa.gov/EPIC/api/natural/images?api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY

# BASE URL
# https://epic.gsfc.nasa.gov/archive/natural


def download_url():
    apikey = 'YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY'
    url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={apikey}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Failed to get data:', response.status_code)


def parse_data(data: dict) -> None:
    base_url = 'https://epic.gsfc.nasa.gov/archive/natural'

    # Construct full image URLs for all images
    image_urls = [f"{base_url}/{datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S').year}/{datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S').month:02d}/{datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S').day:02d}/jpg/{item['image']}.jpg"for item in data]
    # Store the URLs
    store_urls(image_urls)


def runearthimg():
    data = download_url()
    parse_data(data)
    display_imgs()
