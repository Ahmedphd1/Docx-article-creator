from pexels_api import API
import requests
import shutil
from io import BytesIO
from PIL import Image
from io import BytesIO
from random import randrange
import time

PEXELS_API_KEY = '563492ad6f9170000100000108c27ac22faf4eb3877754459c8cc238'

api = API(PEXELS_API_KEY)

def findimage(listoftext):
    listofimages = []

    print("Trying to find images")

    for i in listoftext:
        try:
            start = int(len(i) / 2)
            end = len(i)

            myword = i[start:end].split(" ")[randrange(len(i[start:end].split(" ")))]
        except:
            print("cannot find word")
            myword = "Dog"

        try:
            api.search(myword, page=1, results_per_page=5)

            photos = api.get_entries()

            response = requests.get(photos[0].medium, stream=True)

            myimage = BytesIO(response.content)

            listofimages.append(myimage)

            time.sleep(2)
        except:
            print("cannot find image")
            continue
    print("Images found: exiting")
    return listofimages