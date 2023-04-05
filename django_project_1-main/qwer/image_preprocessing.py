from PIL import Image
import numpy as np
import cv2



def dbobject_to_np(db_object):
    img_path = db_object.image.path
    img_pil = Image.open(img_path).convert('RGB')
    img_np = np.array(img_pil)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    return img_cv


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
