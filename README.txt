wp4.py is a program that allows the user to interact with
NASA's web API. The user can view images from the curiosity
mars rover, or the earth polychromatic imaging camera.

The program calls the needed api and then parses the response.
It stores the urls for the images in a urls.txt file in the directory.
Then it selects a random url and displays the image using matplotlib.