"""
This module contains functions to download and parse data
from the NASA Mars Rover Photos API. It uses the API key to
make a request to the API, parses the returned data to extract
image URLs, and then stores these URLs for later use.
"""


import requests
from fileio import store_urls
from display_imgs import display_imgs

# API KEY
# YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY

# EXAMPLE URLS
# https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol=1000&camera=pancam&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY
# https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY
# https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY
# https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=,mast&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY


def download_url():
    ''' Calls the API and returns the data in json format'''
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY'

    try:
        response = requests.get(url, timeout=10)
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
    return None


def parse_data(data: dict) -> None:
    ''' Parses the data and stores the image URLs'''
    photolinks = [photo['img_src'] for photo in data['photos']]
    store_urls(photolinks)


def runmarsrover():
    ''' Downloads the data, parses it and displays the images'''
    data = download_url()
    parse_data(data)
    display_imgs()
