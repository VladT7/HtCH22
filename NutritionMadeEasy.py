# Import Libraries
from urllib.request import urlopen
import json
import cv2
from pyzbar import pyzbar

# STEP ONE: Get user criterion
# ask user for criteria
crZero = input("Type one category: ")
crOne = input("Type another category: ")
crTwo = input("Type another category: ")
criteria = [crZero, crOne, crTwo]


# Function Identifies Barcode
def read_barcodes(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y, w, h = barcode.rect
        # 1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

        # 3
        with open("barcode_result.txt", mode='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
            nutrition_value(barcode_info)
    return frame


def nutrition_value(barcode_info):
    # store the URL in url as
    # parameter for urlopen
    upc = barcode_info
    url = "https://world.openfoodfacts.org/api/v0/product/{upcToPass}.json".format(
        upcToPass=upc)

    # store the response of URL
    response = urlopen(url)

    # storing the JSON response
    # from url in data
    product_json = json.loads(response.read())

    # find name of product

    product_name = ' '.join(
        product_json['product']['product_name'].split(' '))

    print(product_name)

    # pictures of product scanned

    products_images_display = product_json['product']['image_front_url']
    products_images_thumb = product_json['product']['image_front_thumb_url']
    products_images_small = product_json['product']['image_front_small_url']

    print('Display picture of {product}: {display}'.format(
        product=product_name, display=products_images_display))
    print('Thumb picture of {product}: {thumb}'.format(
        product=product_name, thumb=products_images_thumb))
    print('Small picture of {product}: {small}'.format(
        product=product_name, small=products_images_small))
    # STEP THREE: cross references
    crit_levels = []
    for i in criteria:
        crit_levels.append(product_json['product']['nutrient_levels'][i])

    # print("CritLevels:", crit_levels)
    # get the most specific classification of the product scanned
    specific_cat = product_json['product']['categories_hierarchy'][-1][3:]
    # print("Specific category, ", specific_cat)

    # get the scanned product's nutrition values per 100g
    val_c0 = product_json['product']['nutriments']['{}_100g'.format(criteria[0])]
    val_c1 = product_json['product']['nutriments']['{}_100g'.format(criteria[1])]
    val_c2 = product_json['product']['nutriments']['{}_100g'.format(criteria[2])]

    criterion_values = [val_c0, val_c1, val_c2]

    # want to see what the values are?
    # for i in criterion_values:
    #     print(i)

    # if there is any critLevel other than 'low', then it is not healthy, so we need to suggest better options

    # figure out operators to use based on crit_levels

    op = []
    if crit_levels[0] == 'low' and crit_levels[1] == 'low' and crit_levels[2] == 'low':
        print("This product is healthy!")
    else:
        for i in range(0, len(crit_levels)):
            if crit_levels[i] == 'low':
                op.append('lte')
            elif crit_levels[i] == 'high' or crit_levels[i] == 'moderate':
                op.append('lt')
            print(criteria[i], op[i], criterion_values[i])

    new_url = "https://world.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0" \
              "=contains&tag_0={category}&nutriment_100g_0={criterionZero}&nutriment_100g_compare_0={" \
              "opZero}&nutriment_100g_value_0={val_c0}&nutriment_1={criterionOne}&nutriment_compare_1={" \
              "opOne}&nutriment_value_1={val_c1}&nutriment_2={criterionTwo}&nutriment_compare_2={" \
              "opTwo}&nutriment_value_2={val_c2}&sort_by=nutriscore_score&json=true".format(
        category=specific_cat, criterionZero=crZero, opZero=op[0], opOne=op[1], opTwo=op[2], val_c0=criterion_values[0],
        criterionOne=crOne, val_c1=criterion_values[1], criterionTwo=crTwo, val_c2=criterion_values[2])

    # print(new_url)

    similar_cat_url = urlopen(new_url)
    similar_cat_json = json.loads(similar_cat_url.read())

    suggest_products = similar_cat_json['products'][0]['product_name']

    suggest_products_images_display = similar_cat_json['products'][0]['image_front_url']
    suggest_products_images_thumb = similar_cat_json['products'][0]['image_front_thumb_url']
    suggest_products_images_small = similar_cat_json['products'][0]['image_front_small_url']

    print("You should try", suggest_products)
    print("Here is the biggest picture of it:",
          suggest_products_images_display)

    print("Here is the thumbnail picture of it:",
          suggest_products_images_thumb)

    print("Here is the smallest picture of it:",
          suggest_products_images_small)
    Output_Dict = {"CriteriaZero": criteria[0], "CriteriaOne": criteria[1], "CriteriaTwo": criteria[2], "CriteriaZeroLevel": crit_levels[0], "CriteriaOneLevel": crit_levels[1], "CriteriaTwoLevel": crit_levels[2], "CriteriaZeroValue": criterion_values[0], "CriteriaOneValue": criterion_values[1],
                "CriteriaTwoValue": criterion_values[2], "ProductName": product_name, "ProductImage": products_images_display, "ProductImageSM": products_images_thumb, "SuggestedProduct": suggest_products, "SuggestedProductImg": suggest_products_images_display, "SuggestedProductImgSM": suggest_products_images_thumb}

    finalOutputAsJSON(Output_Dict)  
    return barcode_info


def main():
    # 1
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    # 2
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    # 3
    camera.release()
    cv2.destroyAllWindows()

def finalOutputAsJSON(input):
    jsonObject = json.dumps(input)
    print(jsonObject)
    with open("./json/results.json", "w") as outfile:
        outfile.write(jsonObject)




# initialization of main
if __name__ == '__main__':
    main()
    