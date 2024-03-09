import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO
import requests
import random
from fileio import retrieve_urls


def display_imgs():
    photolinks = retrieve_urls()
    random_image_src = random.choice(photolinks)
    response = requests.get(random_image_src)
    img = mpimg.imread(BytesIO(response.content), format='JPG')
    plt.imshow(img)
    plt.show()
