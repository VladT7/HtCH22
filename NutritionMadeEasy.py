# Import Libraries
from urllib.request import urlopen
import json
import cv2
from pyzbar import pyzbar



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

        if barcode_info != "":
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
    data_json = json.loads(response.read())

    # print the name of product
    print(' '.join(data_json['product']['_keywords']))

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


# 4
if __name__ == '__main__':
    main()
