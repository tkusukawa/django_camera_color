import cv2
import base64
import numpy as np
import io

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!")

def camera(request):
    data = {
        'app': 'Camera',
        'nums': [2,3,5,7,11,13,17],

    }
    return render(request, "camera/camera.html", data)

def read(request):
    #print('hogehoge')
    #print(request)
    b64image = request.POST.get('image')
    # print(b64image)

    image =base64.b64decode(b64image)
    #print(type(image))

    jpg=np.frombuffer(image, dtype=np.uint8)
    #print(type(jpg))
    #raw image <- jpg
    raw_img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
    #print(type(raw_img))
    #print(raw_img.shape)
    height = raw_img.shape[0]
    width = raw_img.shape[1]
    x = int(width / 2)
    y = int(height / 2)

    #imgBox = raw_img[y:(y+1), x:(x+1)]
    #b = imgBox.T[0].flatten().mean()
    #g = imgBox.T[1].flatten().mean()
    #r = imgBox.T[2].flatten().mean()
    b = raw_img[y, x, :][0]
    g = raw_img[y, x, :][1]
    r = raw_img[y, x, :][2]
    print([r,g,b])
 
    #画像を保存する場合
    cv2.imwrite("image.jpg",raw_img)

    d = {
        'r': r,
        'g': g,
        'b': b,
    }
    return JsonResponse(d)
