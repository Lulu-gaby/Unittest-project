import requests

def get_random_cat_image():
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    if response.status_code == 200:
        return response.json()[0]["url"]
    return None