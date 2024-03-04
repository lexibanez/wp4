import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO
import requests
import random
from fileio import store_urls, retrieve_urls

# API KEY
# YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY

# EXAMPLE URL
# https://api.nasa.gov/mars-photos/api/v1/rovers/opportunity/photos?sol=1000&camera=pancam&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY
# https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY
# https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY
# https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=,mast&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY

def download_url():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=YccDa6K8L7Vcxa9DvtEuDyWR4M49CPiEQ3xuKNaY'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print('Failed to get data:', response.status_code)


def parse_data(data: dict) -> None:
    photolinks = [photo['img_src'] for photo in data['photos']]
    store_urls(photolinks)


def display_imgs():
    photolinks = retrieve_urls()
    random_image_src = random.choice(photolinks)
    response = requests.get(random_image_src)
    img = mpimg.imread(BytesIO(response.content), format='JPG')
    plt.imshow(img)
    plt.show()


def main():
    data = download_url()
    parse_data(data)
    display_imgs()
    

if __name__ == '__main__':
    main()
    