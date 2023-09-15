import pandas as pd
from model import model
from image import image_import
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image


class similar_visual:

    def __init__(self, size:int=224, predict_name:str='test'):
        '''
        Input
        1) size
            : 모델에 입력할 이미지 사이즈 지정 (기본값 = 224)
        2) predict_name
            : 모델학습시 예측값을 저장할 파일(.npy)이름
        Output
        1) _similar_all
            : 캐릭터간 코사인 유사도를 시각화한 자료
        2) _similar_one(name)
            : 선택한 캐릭터의 이름과 유사도가 높은 10개를 보여줌
        Note
            1) 입력된 데이터의 코사인 유사도를 구하고 시각화해주는 함수

        '''
        self.self = self
        self._img_size = size
        self.pre_name = predict_name
        

    def _similar_model(self):
        
        # 모델생성
        vgg16_model = model.model_all()._vgg16()
        print("<<<  vgg16 모델이 정상적으로 생성되었습니다.   >>>")

        # 데이터를 불러옴
        data, data_name = image_import(self._img_size)._image_pokemon()

        if len(data) == len(data_name):
            print(f"<<< 이미지 {len(data)}개를 정상적으로 불러왔습니다. >>>")
            print("**********    이미지를 모델에 적용합니다.    ********** ")

            if os.path.exists(f"./predict_data/{self.pre_name}.npy"):
                print(f"<{self.pre_name}_array> 이름이 이미 존재함으로 해당 파일을 이용하여 유사도를 확인합니다.")
                X_vgg = np.load(f"./predict_data/{self.pre_name}.npy")
            else:
                if self.pre_name == '':
                    # 이름이 default 값이면 따로 저장하지 않고 학습진행
                    print("데이터를 vgg 모델에 적용합니다.")
                    X_vgg = vgg16_model.predict(data)
                else:
                    print("이전에 학습된 파일이 존재하지 않아 데이터를 vgg16 모델에 적용합니다.")
                    X_vgg = vgg16_model.predict(data)
                    np.save(f"./predict_data/{self.pre_name}.npy", X_vgg)

            df_x_vgg = pd.DataFrame(X_vgg)
            df_x_vgg.index = data_name
            df_x_vgg.index.name = "name"
            return df_x_vgg, data, data_name
        
        else:
            print("<<< 이미지와 이름이 매치되지 않습니다. >>>")


    def _visualization_all(self):  

        df_x_vgg, data, data_name = self._similar_model()
       

        user_based_collabor = cosine_similarity(df_x_vgg)
        
        user_based_collabor = pd.DataFrame(user_based_collabor, index=df_x_vgg.index, columns=df_x_vgg.index)
    
        print("***************************************************************")
        print("********** 이미지별 코싸인 유사도는 아래와 같습니다. **********")
        
        return print(user_based_collabor)
    
    def _visualization_one(self, name):

        df_x_vgg, data, data_name = self._similar_model()
        user_based_collabor = cosine_similarity(df_x_vgg)
        user_based_collabor = pd.DataFrame(user_based_collabor, index=df_x_vgg.index, columns=df_x_vgg.index)

        sim_df = pd.DataFrame(user_based_collabor[name].sort_values(ascending=False).reset_index())
        sim_df.columns = ['name', 'similarity']
        sim_df = sim_df[sim_df['name'] != name][:10]
        sim_df['similarity'] = sim_df['similarity'].round(3)
        
        
        print(f"\n=========== {name}과 비슷한 유형인 포켓몬 TOP 10 ===========")

        list_name = []
        list_sim = []

        for i in range(len(sim_df)):
            prob_id = sim_df['name'].iloc[i]
            print("TOP",i+1, "(",sim_df['similarity'].iloc[i],") : ", prob_id)
            list_name.append(prob_id)
            list_sim.append(sim_df['similarity'].iloc[i])


        selected_classes = sim_df['name'].values
        selected_images = []
        selected_img_sim = sim_df['similarity'].values

        # 이미지 값을 순서대로 받아오기 위한 구문(지정하지 않을시 인식한 순서대로 저장됨)
        for target_class in selected_classes:
            for i, label in enumerate(data_name):
                if label == target_class:
                    selected_images.append(data[i])
                
            

        selected_images = np.array(selected_images)

        # 3x5 그리드로 이미지 표시
        fig, axes = plt.subplots(3, 5, figsize=(15, 6))

        top_image_path = f"./pokemon/images/images/{name}.png"
        top_image = Image.open(top_image_path)
        # 첫번째 행에 대상 이미지 삽입
        axes[0, 0].imshow(top_image)
        axes[0,0].axis('off')
        axes[0, 0].set_title(f"comparison target : {name}")
        axes[0,1].axis('off')
        axes[0,2].axis('off')
        axes[0,3].axis('off')
        axes[0,4].axis('off')

        for i in range(2):
            for j in range(5):
                index = i * 5 + j
                if index < len(selected_images):
                    axes[i+1, j].imshow(selected_images[index])
                    axes[i+1, j].set_title(selected_classes[index] + f'<{selected_img_sim[index]:.3f}>')
                    axes[i+1, j].axis('off')
                else:
                    axes[i+1, j].axis('off')
        plt.tight_layout()
        return plt.show()
                