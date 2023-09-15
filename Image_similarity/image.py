import os
import cv2
import glob
import numpy as np




class image_import:
    
    
    def __init__(self, image_size:int=224):
        
        self.self = self
        self.image_size = image_size
    

    def _image_pokemon(self):
        
        img_dir = "./pokemon/images/images" # 이미지 경로

        X = []
        y = [] 

        data_path = os.path.join(img_dir,'*g') 
        files = glob.glob(data_path)
        
        
        for f1 in files:
            try:

                img = cv2.imread(f1) # 이미지 파일을 읽어드림
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 이미지를 rgb값으로 변환(혹 rgb값이 아닌것이 있을까봐)
                img = cv2.resize(img, (self.image_size, self.image_size)) # 이미지 크기를 원하는 사이즈로 변경
                
                X.append(np.array(img)) # 이미지를 배열로 변환
                y.append(os.path.basename(f1).split('.')[0])
                
            
            except :
                continue

        X = np.array(X)
        y = np.array(y)

        return X, y

            
