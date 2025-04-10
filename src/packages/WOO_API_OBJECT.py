import woocommerce
import json

from . import TypeDefs

with open("apikeys.env") as file:
    API_KEYS: TypeDefs.APIKeys = json.load(file)

wooAPIObj = woocommerce.API(
    url="https://kaikas69.web-seminars.eu",
    consumer_key = API_KEYS["consumer_key"],
    consumer_secret = API_KEYS["consumer_secret"],

    wp_api = True,
    version = "wc/v3",

    timeout = 15
)