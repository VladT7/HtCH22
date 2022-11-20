from urllib.request import urlopen
import json

# STEP ONE: Get user criterion
# ask user for criteria
crZero = input("Type one category: ")
crOne = input("Type another category: ")
crTwo = input("Type another category: ")
criteria = [crZero, crOne, crTwo]

# STEP TWO: Scan Barcode and get JSON
upc = input("Enter UPC:")
url = "https://world.openfoodfacts.org/api/v0/product/{upcToPass}.json".format(
    upcToPass=upc)

# store the response of URL
response = urlopen(url)
# storing the JSON response from url
product_json = json.loads(response.read())

# find name of product

productName = ' '.join(
    product_json['product']['product_name'].split(' '))
print(productName)

# STEP THREE: cross references
critLevels = []
for i in criteria:
    critLevels.append(product_json['product']['nutrient_levels'][i])

#print("CritLevels:", critLevels)
# get the most specific classifaction of the product scanned
specificCat = product_json['product']['categories_hierarchy'][-1][3:]
#print("Specific category, ", specificCat)

# get the scanned product's nutrition values per 100g
val_c0 = product_json['product']['nutriments']['{}_100g'.format(criteria[0])]
val_c1 = product_json['product']['nutriments']['{}_100g'.format(criteria[1])]
val_c2 = product_json['product']['nutriments']['{}_100g'.format(criteria[2])]

criterionValues = [val_c0, val_c1, val_c2]

# want to see what the values are?
# for i in criterionValues:
#     print(i)

# if there is any critLevel other than 'low', then it is not healthy, so we need to suggest better options

# figure out operators to use based on critLevels


op = []
if critLevels[0] == 'low' and critLevels[1] == 'low' and critLevels[2] == 'low':
    print("This product is healthy!")
else:
    for i in range(0, len(critLevels)):
        if critLevels[i] == 'low':
            op.append('lte')
        elif critLevels[i] == 'high' or critLevels[i] == 'moderate':
            op.append('lt')


newUrl = "https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0={category}&nutriment_100g_0={criterionZero}&nutriment_100g_compare_0={opZero}&nutriment_100g_value_0={val_c0}&nutriment_1={criterionOne}&nutriment_compare_1={opOne}&nutriment_value_1={val_c1}&nutriment_2={criterionTwo}&nutriment_compare_2={opTwo}&nutriment_value_2={val_c2}&json=true".format(
    category=specificCat, criterionZero=crZero, opZero=op[0], opOne=op[1], opTwo=op[2], val_c0=criterionValues[0], criterionOne=crOne, val_c1=criterionValues[1], criterionTwo=crTwo, val_c2=criterionValues[2])

similarCatUrl = urlopen(newUrl)
similarCatJson = json.loads(similarCatUrl.read())
