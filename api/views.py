# Create your views here.
from django.views import View
import json
from django.http import JsonResponse
from .models import Musicians
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import base64
from io import BytesIO


def BarcodeReader(base64_image):
    # Decode the base64 string to bytes
    image_data = base64.b64decode(base64_image)

    # Convert the bytes to a NumPy array
    nparr = np.frombuffer(image_data, np.uint8)

    # Decode the NumPy array to an OpenCV image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # The rest of your barcode decoding logic remains unchanged
    detectedBarcodes = decode(img)

    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        for barcode in detectedBarcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(
                img, (x - 10, y - 10), (x + w + 10, y + h + 10), (255, 0, 0), 2
            )

            if barcode.data != "":
                print(barcode.data)
                # print(barcode.type)
                return {"barcode_data": barcode.data.decode("utf-8")}
                # return json.dumps({"barcode": barcode.data})

    # cv2.imshow("Image", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# from django.contrib.auth import authenticate
class save_musicians(View):
    def get(self, request):
        return JsonResponse({"message": "nice"})

    def post(self, request):
        jd = json.loads(request.body)
        image = jd["image"]
        res = BarcodeReader(image)
        print(res, "heree")
        return JsonResponse({"message": res})
