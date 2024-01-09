# Create your views here.
from django.views import View
import json
from django.http import JsonResponse
from pyzbar.pyzbar import decode
import base64
import io

from PIL import Image


def BarcodeReader(base64_image):
    image_data = base64.b64decode(base64_image)
    pil_image = Image.open(io.BytesIO(image_data))
    detected_barcodes = decode(pil_image)
    if not detected_barcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        for barcode in detected_barcodes:
            print(barcode.data)
            return {"barcode_data": barcode.data.decode("utf-8")}


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
