import time
import os
from celery import shared_task
from django.core.mail import EmailMessage
import cv2
import numpy as np
from io import BytesIO
import json

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

@shared_task(bind=True)
def create_task(self, email=None, image=None):
    # Given according to the standard strip format
    parameter_names = ['URO', 'BIL', 'KET', 'BLD', 'PRO', 'NIT', 'LEU', 'GLU', 'SG', 'PH']

    image_np = np.frombuffer(image, np.uint8)
    image = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    # pixel coordinates along with width and height
    box_coordinates = [(133, 47, 39, 40), (133, 123, 39, 40), (133, 130, 39, 40), (133, 224, 39, 40), (133, 309, 39, 40),
                   (133, 487, 39, 40), (133, 576, 39, 40), (133, 666, 39, 40), (133, 760, 39, 40), (133, 854, 39, 40)]

    finalAns = []
    for (x, y, width, height) in box_coordinates:
        roi = image[y:y+height, x:x+width]
        average_color = (np.mean(roi, axis=(0, 1)))
        finalAns.append(average_color)

    result_dict = {parameter_names[i]: finalAns[i] for i in   range(len(parameter_names))}
    result_string = json.dumps(result_dict, cls=NumpyEncoder, indent=4)
    # Send email using the result produced above
    email = EmailMessage(
        subject="Regarding the Urine Strip Analysis Results",
        body=str(result_string),
        from_email=os.environ.get("EMAIL_FROM"),
        to=[email],
    )
    email.send()
    return True