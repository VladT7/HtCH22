from urllib.request import urlopen

# import json
import json
# store the URL in url as
# parameter for urlopen
upc = input("Enter UPC:")
url = "https://world.openfoodfacts.org/api/v0/product/{upcToPass}.json".format(
    upcToPass=upc)

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())

# print the name of product
print(' '.join(data_json['product']['_keywords']))
