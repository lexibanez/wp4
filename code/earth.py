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
    ''' Calls the API and returns the data in json format
    '''
    apikey = 'YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY'
    url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={apikey}'

    try:
        response = requests.get(url)
        # Raises a HTTPError if the status is 4xx, 5xx
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error: ", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting: ", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error: ", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong with the request: ", err)


def parse_data(data: dict) -> None:
    ''' Parses the data and stores the image URLs'''

    base_url = 'https://epic.gsfc.nasa.gov/archive/natural'

    # Construct full image URLs for all images
    image_urls = [f"{base_url}/{datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S').year}/{datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S').month:02d}/{datetime.strptime(item['date'], '%Y-%m-%d %H:%M:%S').day:02d}/jpg/{item['image']}.jpg"for item in data]
    # Store the URLs
    store_urls(image_urls)


def runearthimg():
    ''' Downloads the data, parses it and displays the images
    '''
    data = download_url()
    parse_data(data)
    display_imgs()
