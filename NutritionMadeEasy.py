# Read barcode

# Import Libraries
import string

import cv2
from pyzbar import pyzbar
from nutritionix import Nutritionix


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
    # app_id and api_key from nutrionix.com
    app_id = "6d76cb9b"
    api_key = "46e90bb9e25ed79df04660e366471b2b	—"
    nix = Nutritionix(app_id, api_key)
    barcode_item = nix.search(upc=int(barcode_info))
    print(barcode_item)
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
