from PIL import Image
import numpy as np
import cv2

import onnxruntime as ort
import time, cv2, PIL
import numpy as np
from tqdm.notebook import tqdm
import glob


# providers = ['CPUExecutionProvider']

def dbobject_to_np(db_object):
    img_path = db_object.search_image.path
    img_pil = Image.open(img_path).convert('RGB')
    img_np = np.array(img_pil)
    return  cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)




def ani_to_edge(ani_image): 
    gray_img =  cv2.cvtColor(ani_image , cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray_img,invertedblur, scale=256.0)
    return sketch

def np_to_pil(img_np):
    # NumPy 배열을 PIL 이미지로 변환
    return Image.fromarray(np.uint8(img_np))


def process_image(img, x32=True):
    h, w = img.shape[:2]
    if x32: # resize image to multiple of 32s
        def to_32s(x):
            return 256 if x < 256 else x - x%32
        img = cv2.resize(img, (to_32s(w), to_32s(h)))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32)/ 127.5 - 1.0
    return img


def Convert(img, scale,session):
    x = session.get_inputs()[0].name
    y = session.get_outputs()[0].name
    fake_img = session.run(None, {x : img})[0]
    images = (np.squeeze(fake_img) + 1.) / 2 * 255
    images = np.clip(images, 0, 255).astype(np.uint8)
    output_image = cv2.resize(images, scale[::-1])
    print(x,y)
    return  cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR)

def image_sharpening(np_image):
# 커널 생성(대상이 있는 픽셀을 강조)
    kernel = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])
    return cv2.filter2D(np_image, -1, kernel)


   



def real(np_image):
    pic_form = ['.jpeg','.jpg','.png','.JPEG','.JPG','.PNG']
    device_name = ort.get_device()
    providers = ['CPUExecutionProvider']
    model = 'AnimeGANv2_Hayao' 
    session = ort.InferenceSession(f'coloring/{model}.onnx', providers=providers)
    ANI_img = np_image.astype(np.float32)
    img1 = process_image(ANI_img)
    img2 = np.expand_dims(img1, axis=0)
    mat = img2 
    scale = ANI_img.shape[:2]
    res = Convert(mat, scale,session)
    print('됐다')
    res=ani_to_edge(res)
    hard = image_sharpening(res)
   
    ###############

    img1 = process_image(res)
    img2 = np.expand_dims(img1, axis=0)
    mat = img2 
    scale = res.shape[:2]
    res = Convert(mat, scale,session)
    print('됐다')
    res=ani_to_edge(res)
    easy =image_sharpening(res)
    return hard,easy
