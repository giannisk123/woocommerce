# python -m src.trelo (curr dir: woocommerce)

# global libraries
import json
from typing import TypedDict

# own stuff
from .packages import TypeDefs
from . import Products as productUtility


# create the woocommerce API wrapper object


# Static dictionaries
DEFINED_PRODUCTS = productUtility.DefinedProducts
CATEGORY_IDS = productUtility.CategoryIDs

allWebCreatedProducts = productUtility.allWebCreatedProducts

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
        alreadyCreatedVariation: TypeDefs.variation = product["variations"]

        for _, attribute in enumerate(product["attributes"]):
            if attribute["variation"] == True:
                correspondingVariationData = product["variations"][attribute["name"]]
                postData.append(correspondingVariationData)


print(json.dumps(allWebCreatedProducts, indent=4))