from typing import Any, TypedDict
from typing import Optional
from typing import Literal
from typing import Union

################################################################ Images #####################################################

class _newImage(TypedDict):
    src: str

class _existingImage(TypedDict):
    id: int

class _category(TypedDict):
    id: str
#############################################################################################################################


################################################################ Attributes #####################################################

class _baseAttribute(TypedDict):
    variation: bool
    visible: bool
    options: list[str]

class attribute(_baseAttribute):
    id: int
    name: str

class default_attribute(attribute):
    option: str

class variation(TypedDict):
    id: Optional[int]

    regular_price: str
    image: _newImage | _existingImage
    attributes: list[default_attribute]

#####################################################################################################################

class APIKeys(TypedDict):
    consumer_key: str
    consumer_secret: str

class SimpleProduct(TypedDict):
    name: str
    type: Literal["simple", "variable"]
    regular_price: str
    description: str
    short_description: str
    categories: list[_category]  # Category ID for the product (you need to find the category ID)
    images: list[_newImage | _existingImage]  # Image URL
    stock_status: Literal["instock", "outofstock"]

class VariableProduct(SimpleProduct):
    attributes: list[attribute]
    default_attributes: Optional[list[default_attribute]]
    variations: list[variation]