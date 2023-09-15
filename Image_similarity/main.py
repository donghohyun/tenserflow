from similar import similar_visual
import click

from image import image_import


@click.command()
@click.option('-a', '--batch-one-all', type = click.STRING, default = 'all', help = '유사도를 전체를 출력할지 한개를 대상으로 비교할지 선정(one or all)')
@click.option('-n', '--batch-name', type = click.STRING, default = 'abomasnow', help = '비교하고자 하는 캐릭터 이름을 입력하세요')
@click.option('-f', '--file-name', type = click.STRING, default = '', help = '돌릴때 마다 모델을 돌릴시 시간이 오래걸리므로 학습한 데이터를 저장하기 위한 파일명임')
def start_batch(batch_one_all,batch_name, file_name):
    
    _one_all = ["one","all"]
    if batch_one_all not in _one_all:
        print("************************************************************************************\n")
        print("<<<  유사도 전체를 출력하려면 -a값으로 all을 특정 캐릭터값만 보려면 one을 입력하세요 >>>\n")
        print("************************************************************************************")
    
    
    a,image_name = image_import(224)._image_pokemon()
    if batch_name not in image_name:
        print(f"\n <<<<<<<<<    입력한 <{batch_name}>와 일치하는 이름의 포켓몬이 없습니다.      >>>>>>>>>")
        print("*********   아래 리스트 중 비교하고자 하는 포켓몬이름을 입력해 주세요   *********")
        print(image_name)
        
    else:
    
    
        if batch_one_all == 'all':
            similar_visual(size = 224, predict_name= file_name)._visualization_all()
        
        elif batch_one_all == 'one':
            similar_visual(size = 224, predict_name= file_name)._visualization_one(batch_name)



if __name__ == '__main__':
    start_batch()

