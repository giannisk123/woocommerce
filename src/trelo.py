# python -m src.trelo (curr dir: woocommerce)

# global libraries
import json
from typing import TypedDict
import woocommerce

# own stuff
from .packages import TypeDefs
from . import Products as productUtility

with open("apikeys.env") as file:
    API_KEYS: TypeDefs.APIKeys = json.load(file)

# create the woocommerce API wrapper object
wooAPIObj = woocommerce.API(
    url="https://kaikas69.web-seminars.eu",
    consumer_key = API_KEYS["consumer_key"],
    consumer_secret = API_KEYS["consumer_secret"],

    wp_api = True,
    version = "wc/v3",

    timeout = 15
)

# Static dictionaries
DEFINED_PRODUCTS = productUtility.DefinedProducts
CATEGORY_IDS = productUtility.CategoryIDs

allWebCreatedProducts: list[TypeDefs.VariableProduct] = wooAPIObj.get("products").json() # type:ignore

def SyncLocalProductListToWeb():
    productsToCreate: list[TypeDefs.VariableProduct] = []
    productsToUpdate: list[TypeDefs.VariableProduct] = []

    for _, product in enumerate(DEFINED_PRODUCTS):
        alreadyCreatedProduct = productUtility.FindFirstProductFromName(allWebCreatedProducts, product["name"])

        if not alreadyCreatedProduct:
            print(f"New product: {product["name"]}")
            productsToCreate.append(product)
        else:
            productsToUpdate.append(product)
            print("Product already exists")
            
    if len(productsToCreate) > 0:
        print("Creating new products...")

        wooAPIObj.post("products/batch", {"create": productsToCreate}) # type:ignore
    else:
        print("No new products to create.")
    
    if len(productsToUpdate) > 0:
        print("Updating products...")
        wooAPIObj.post("products/batch", {"update": productsToUpdate}) # type:ignore
    
def SyncProductVariations(products: list[TypeDefs.VariableProduct]):
    for _, product in enumerate(products):
        postData: list[TypeDefs.variation] = []
        alreadyCreatedVariation: TypeDefs.variation = product["variations"][] # type:ignore
        alreadyCreatedVariation
        for _, attribute in enumerate(product["attributes"]):
            if attribute["variation"] == True:
                correspondingVariationData = product["variations"][attribute["name"]]
                postData.append(correspondingVariationData)
        
