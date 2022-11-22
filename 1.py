import os
import cv2
import matplotlib.pyplot as plt
def cvt_image_save(dir_path:str)->list:# cat_img_download'
  files_names =  [name for name in os.listdir(dir_path)]
  
  print(files_names)
  cvt_images=[]
  for i , file_name in enumerate(files_names):
    # print(os.path.join(dir_path,file_name))
    path = os.path.join(dir_path,file_name)
    image = cv2.imread(path)

    cvt_image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
    cvt_images.append(cvt_image)

  return cvt_images

cvt_image = cvt_image_save('puppy_img_download')
plt.imshow(cvt_image[0])
plt.show()

