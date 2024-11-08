import requests

r_search = requests.post(
    "https://www.migros.ch/product-display/public/v4/product-cards",
    headers=headers,
    json=payload,
)


def load_products_list():
    product_ids = []

    with open("product_ids.txt") as f:
        for line in f.readlines():
            if line[-1] == "\n":
                product_ids.append(line[:-1])
            else:
                product_ids.append(line)

    return product_ids


def get_products_data():
    r_token = requests.get(
        "https://www.migros.ch/authentication/public/v1/api/guest?authorizationNotRequired=true"
    )
    token = r_token.headers["leshopch"]

    headers = {"leshopch": token, "migros-language": "fr"}

    payload = {
        "offerFilter": {
            "storeType": "OFFLINE",
            "region": "national",
        },
        "productFilter": {"uids": [*product_ids]},
    }
