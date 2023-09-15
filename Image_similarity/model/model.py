from tensorflow.keras.applications import vgg16
from tensorflow.keras.models import Model



class model_all:
    def __init__(self):
        self.model = vgg16


    def _vgg16(self):

        model = vgg16
        base_model = model.VGG16(weights = "imagenet")
        vgg16_model = Model(inputs=base_model.input, outputs=base_model.get_layer("fc1").output )
        
        return vgg16_model
    
    


            
           
        
        