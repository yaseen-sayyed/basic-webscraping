from bs4 import BeautifulSoup
import requests
from io import BytesIO
import PIL
from PIL import Image
import os


def start_search():
    search = input("Search for: ")
    params = {"q": search}

    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs("./scraped_images/" + dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)
    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.find_all("a", {"class": "thumb"})

    for item in links:
        try:
            img_object = requests.get(item.attrs["href"])
            print("Getting", item.attrs["href"])
            title = item.attrs["href"].split("/")[-1].partition("?")[0]
            try:
                img = Image.open(BytesIO(img_object.content))
                img.save("./" + dir_name + "/" + title)
            except (PIL.UnidentifiedImageError, OSError):
                print("Erroneous image or couldn't save image.")
        except:
            print("Could not get image.")

    start_search()


start_search()
