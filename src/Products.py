from .packages import TypeDefs
from .packages import WOO_API_OBJECT

wooAPIObj = WOO_API_OBJECT.wooAPIObj
allWebCreatedProducts: list[TypeDefs.VariableProduct] = wooAPIObj.get("products").json() # type:ignore

def FindFirstProductFromName(products: list[TypeDefs.VariableProduct], name: str) -> TypeDefs.VariableProduct:
    for _, product in enumerate(products):
        if product["name"] == name:
            return product
    
    return None # type:ignore

def FindFirstVariationFromAttributeCombo(variations: list[TypeDefs.variation], attributes: list[TypeDefs.attribute]) -> TypeDefs.variation:
    """
    Args:
        variations (list[TypeDefs.variation]): Expects a list of variation IDs that came from the web (not from the `DEFINED_PRODUCTS` list), since that contains a var ID.
        attributeNames (list[str]): 

    Returns:
        TypeDefs.variation: The variation that has variation names that match `attributeNames`
    """
    for _, var in enumerate(variations):
        matchingNames: list[str] = []
        requestedAttributeNames: list[str] = []

        for _, requestedAttribute in enumerate(attributes):
            requestedAttributeNames.append(requestedAttribute["name"])

        for _, varAttribute in enumerate(var["attributes"]):
            for _, attribute in enumerate(attributes):
                if varAttribute["name"] == attribute["name"]:
                    matchingNames.append(attribute["name"])
        
        if matchingNames == requestedAttributeNames:
            return var
    
    return None #type:ignore

CategoryIDs = {
    "CPUs": "54",
    "GPUs": "53",
    "HardDrives": "56",
    "HDD": "59",
    "Monitors": "52",
    "Motherboards": "55",
    "RAM": "57",
    "SSD": "58",
    "TechStuff": "51",
    "Uncategorized": "50"
}

DefinedProducts: list[TypeDefs.VariableProduct] = [
    {
        "name": "Gigabyte Radeon RX 7600 XT 16GB GDDR6",
        "type": "simple",
        "description": "<p>\u0392\u03b1\u03c3\u03b9\u03ba\u03ac \u03c7\u03b1\u03c1\u03b1\u03ba\u03c4\u03b7\u03c1\u03b9\u03c3\u03c4\u03b9\u03ba\u03ac:</p>\n<ul>\n<li>\u039c\u03bd\u03ae\u03bc\u03b7 16GB GDDR6, 192bit</li>\n<li>PCI Express x16 4.0</li>\n<li>\u039c\u03ad\u03b3\u03b9\u03c3\u03c4\u03b7 \u0391\u03bd\u03ac\u03bb\u03c5\u03c3\u03b7 7680x4320 pixels</li>\n<li>\u039c\u03ae\u03ba\u03bf\u03c2 \u03ba\u03ac\u03c1\u03c4\u03b1\u03c2 281.4 mm</li>\n<li>2x HDMI 2.1, 2x DisplayPort 1.4a</li>\n<li>\u0395\u03bb\u03ac\u03c7\u03b9\u03c3\u03c4\u03b7 \u0399\u03c3\u03c7\u03cd\u03c2 \u03a4\u03c1\u03bf\u03c6\u03bf\u03b4\u03bf\u03c4\u03b9\u03ba\u03bf\u03cd 600 W</li>\n</ul>\n",
        "short_description": "",
        "regular_price": "350",
        "categories": [
            {
                "id": CategoryIDs["GPUs"],
            }
        ],

        "images": [
            {
                "id": 5048,
            }
        ],
        "stock_status": "instock",
        "attributes": [],
        "default_attributes": [],
    },
    
    {
        "name": "GeForce RTX 4070",
        "type": "variable",
        "description": "",
        "short_description": "<p style=\"text-align: left; font-family: verdana;\">\u0392\u03b1\u03c3\u03b9\u03ba\u03ac \u03c7\u03b1\u03c1\u03b1\u03ba\u03c4\u03b7\u03c1\u03b9\u03c3\u03c4\u03b9\u03ba\u03ac:</p>\n<ul>\n<li style=\"text-align: left; font-family: verdana;\">PCI Express x16 4.0</li>\n<li style=\"text-align: left; font-family: verdana;\">\u039c\u03ad\u03b3\u03b9\u03c3\u03c4\u03b7 \u0391\u03bd\u03ac\u03bb\u03c5\u03c3\u03b7 7680&#215;4320 pixels</li>\n<li style=\"text-align: left; font-family: verdana;\">\u039c\u03ae\u03ba\u03bf\u03c2 \u03ba\u03ac\u03c1\u03c4\u03b1\u03c2 261 mm</li>\n<li style=\"text-align: left; font-family: verdana;\">1x HDMI 2.1, 3x DisplayPort 1.4a</li>\n<li style=\"text-align: left; font-family: verdana;\">\u0395\u03bb\u03ac\u03c7\u03b9\u03c3\u03c4\u03b7 \u0399\u03c3\u03c7\u03cd\u03c2 \u03a4\u03c1\u03bf\u03c6\u03bf\u03b4\u03bf\u03c4\u03b9\u03ba\u03bf\u03cd 650 W</li>\n</ul>\n",
        "regular_price": "",
        "categories": [
            {
                "id": CategoryIDs["GPUs"],
            }
        ],
        "images": [
            {
                "src": "https://kaikas69.web-seminars.eu/wp-content/uploads/2025/03/xlarge_20230428111120_gigabyte_geforce_rtx_4070_12gb_gddr6x_windforce_oc_karta_grafikon_gv_n4070wf3oc_12gd.jpeg",
            }
        ],
        "attributes": [
            {
                "name": "Memory Type",
                "visible": True,
                "variation": True,
                "options": [
                    "GDDR6",
                    "GDDR6X"
                ]
            }
        ],
        "stock_status": "instock",
        "default_attributes": [],
    },
    
    {
        "name": "GeForce RTX TESTTTT XDDD",
        "type": "variable",
        "description": "",
        "short_description": "<p style=\"text-align: left; font-family: verdana;\">\u0392\u03b1\u03c3\u03b9\u03ba\u03ac \u03c7\u03b1\u03c1\u03b1\u03ba\u03c4\u03b7\u03c1\u03b9\u03c3\u03c4\u03b9\u03ba\u03ac:</p>\n<ul>\n<li style=\"text-align: left; font-family: verdana;\">PCI Express x16 4.0</li>\n<li style=\"text-align: left; font-family: verdana;\">\u039c\u03ad\u03b3\u03b9\u03c3\u03c4\u03b7 \u0391\u03bd\u03ac\u03bb\u03c5\u03c3\u03b7 7680&#215;4320 pixels</li>\n<li style=\"text-align: left; font-family: verdana;\">\u039c\u03ae\u03ba\u03bf\u03c2 \u03ba\u03ac\u03c1\u03c4\u03b1\u03c2 261 mm</li>\n<li style=\"text-align: left; font-family: verdana;\">1x HDMI 2.1, 3x DisplayPort 1.4a</li>\n<li style=\"text-align: left; font-family: verdana;\">\u0395\u03bb\u03ac\u03c7\u03b9\u03c3\u03c4\u03b7 \u0399\u03c3\u03c7\u03cd\u03c2 \u03a4\u03c1\u03bf\u03c6\u03bf\u03b4\u03bf\u03c4\u03b9\u03ba\u03bf\u03cd 650 W</li>\n</ul>\n",
        "regular_price": "500",
        "categories": [
            {
                "id": CategoryIDs["GPUs"],
            }
        ],
        "images": [
            {
                "src": "https://kaikas69.web-seminars.eu/wp-content/uploads/2025/03/xlarge_20230428111120_gigabyte_geforce_rtx_4070_12gb_gddr6x_windforce_oc_karta_grafikon_gv_n4070wf3oc_12gd.jpeg",
            }
        ],
        "attributes": [
            {
                "name": "Memory Type",
                "visible": True,
                "variation": True,

                "options": [
                    "GDDR6",
                    "GDDR6X"
                ]
            }
        ],

        "variations": [
            {
                "regular-price": "100",
                "attributes": [{
                    
                }]
            }
        ],

        "stock_status": "instock",
        "default_attributes": [],
    },
]