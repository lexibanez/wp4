"""
This module contains a function to display images from
URLs. The `display_imgs` function retrieves a list of
URLs from a file, selects a random URL, downloads the image
from the URL, and displays the image using matplotlib.
"""


import random
from io import BytesIO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import requests
from fileio import retrieve_urls


def display_imgs():
    ''' Displays a random image from the list of urls stored in the file'''
    photolinks = retrieve_urls()
    random_image_src = random.choice(photolinks)
    response = requests.get(random_image_src, timeout=10)
    img = mpimg.imread(BytesIO(response.content), format='JPG')
    plt.imshow(img)
    plt.show()
