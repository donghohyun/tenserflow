# tenserflow

----
## cli를 통한 변수선언

1) -a
* 유사도를 모든캐릭터에 대한 값을 확인할지(all), 특정캐릭터와 유사한 상위 캐릭터를 그림과 함께 확인할지(one) 설정가능
* default -> all
* all, one 중 설정 가능
2) -n
* -a 값을 one으로 설정시 적용되며, 해당값에 원하는 캐릭터 입력시 해당캐릭터와 유사도가 높게 나온 10개의 캐릭터에 대해 확인 가능하다
* default -> "abomasnow"
* 데이터에 있는 캐릭터 이름 전부 가능
3) -f
* 같은 데이터를 입력하였을때 반복해서 예측값을 구하는것을 막기위해 예측값을 저장하는 이름에 해당된다.
* 지정한 값이 predict_data에 없다면 모델예측값 구하여 새로 저장하고, predict_data에 있는 변수를 입력한다면 저장되어있는 예측값을 바탕으로 결과를 도출하게된다.
* 해당 변수 미지정시 매 실행마다 모델학습이 진행됨(시간이 오래걸릴수 있음)

---
## 결과물
1) 모든 변수를 default값으로 지정하였을 경우
  * 캐릭터 default 값인 'abomasnow'와 유사한 상위 10개 캐릭터들의 이미지가 유사도와 함께 표시됨
  <p align="center">
    <img src="https://github.com/donghohyun/predictive-modeling/assets/139213175/a9054189-2670-4428-b02e-6515276993fc" weight = 500>
  </p>
  
2) a값을 'all'로 주었을 경우
  * 모든 이미지간 유사도 결과가 표시됨
  <p align="center">
    <img src="https://github.com/donghohyun/predictive-modeling/assets/139213175/a676c496-7443-4620-9c7d-1d4e044f11db" weight = 500>
  </p>
