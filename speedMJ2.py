import PySimpleGUI as sg
import os
from random import choice, shuffle,sample
from datetime import timedelta,datetime
import time
from speedMJ import mk_image_list


# 設定-----------------------------------------------------------------
images = ['m (1).png', 'm (2).png', 'm (3).png', 'm (4).png', 'm (5).png', 'm (6).png', 'm (7).png',
        'p (1).png', 'p (2).png', 'p (3).png', 'p (4).png', 'p (5).png', 'p (6).png', 'p (7).png', 'p (8).png', 'p (9).png',
        's (1).png', 's (2).png', 's (3).png', 's (4).png', 's (5).png', 's (6).png', 's (7).png', 's (8).png', 's (9).png',
        't (1).png', 't (2).png', 't (3).png', 't (4).png', 't (5).png', 't (6).png', 't (7).png'
        ]

first_choice = None
first_key = None
second_choice = None
second_key = None
count = 32


def main():
    global first_choice,second_choice,count
    #麻雀牌を二個ずつにしてシャッフル
    images_list = get_image_2(images*2)
    shuffle(images_list)
    layout = [[sg.Text('麻雀神経衰弱',font=('Helvetica',30))],
              [sg.Button('NEW GAME', key='-new-',mouseover_colors=(0,255), pad=((0,400),(0,0)))],
              [sg.Image(filename=path, key=f'-image1{i}-', pad=((10,10),(50,10)),enable_events=True) for i,path in enumerate(images_list[0:8])],
              [sg.Image(filename=path, key=f'-image2{i}-', pad=((10,10),(0,10)),enable_events=True) for i,path in enumerate(images_list[8:16])],
              [sg.Image(filename=path, key=f'-image3{i}-',pad=((10,10),(0,10)),enable_events=True) for i,path  in enumerate(images_list[16:24])],
              [sg.Image(filename=path, key=f'-image4{i}-',pad=((10,10),(0,10)),enable_events=True) for i,path  in enumerate(images_list[24:32])],
              [sg.Image(filename=path, key=f'-image5{i}-',pad=((10,10),(0,10)),enable_events=True) for i,path  in enumerate(images_list[32:40])],
              [sg.Image(filename=path, key=f'-image6{i}-',pad=((10,10),(0,10)),enable_events=True) for i,path  in enumerate(images_list[40:48])],
              [sg.Image(filename=path, key=f'-image7{i}-',pad=((10,10),(0,10)),enable_events=True) for i,path in enumerate(images_list[48:56])],
              [sg.Image(filename=path, key=f'-image8{i}-',pad=((10,10),(0,10)),enable_events=True) for i,path  in enumerate(images_list[56:64])],
              [sg.Image(filename=path, key=f'-image9{i}-',pad=((10,10),(0,10)),enable_events=True) for i,path  in enumerate(images_list[64:66])],
             ]
    
    window = sg.Window('麻雀',layout,size=(800,800),element_justification='center')

    while True:
        event, values = window.read(timeout=30)
        if event == sg.WINDOW_CLOSED:
            break
        #麻雀牌の選択時
        if event.startswith('-image'):
            #選択が一枚目なら
            if not first_choice:
                first_choice = window[event].Filename
                first_key = window[event].Key
                window[event].update(filename='images\\tupai\\t (2).png', subsample=2)
            #選択が二枚目なら
            else:
                second_choice =window[event].Filename
                second_key = window[event].Key
                #判定
                result =judgement(first_choice,second_choice)
                if result:
                    window[first_key].update(filename="")
                    window[second_key].update(filename="")
                    count -= 1
                    first_choice = None
                else:
                    window[first_key].update(filename=first_choice)
                    first_choice = None
        #新しいゲーム作成
        if event =='-new-':
            shuffle(images_list)
            images_index = 0
            for i in range(8):
                for m in range(8):
                    window[f'-image{i+1}{m}-'].update(filename=images_list[images_index])
                    images_index += 1

        if count == 0:
            sg.popup('おめでとうございます！クリアです')
            break
        else:pass
    window.close()

# def mk_Image_path_list(seq):
#     images =[]
#     for cur, sub, file in os.walk(seq):
#         path = os.path.join(,file)
#         images.append(path)
#     return images

#麻雀牌のパス
def get_image_2(seq):
    path_list = []
    for card in seq:
        if card.startswith('m'):
            path =os.path.join('.\\images\\manz', card)
        elif card.startswith('p'):
            path =os.path.join('.\\images\\pins', card)
        elif card.startswith('s'):
            path = os.path.join('.\\images\\souz',card)
        else:path = os.path.join('.\\images\\tupai', card)
        path_list.append(path)
    return path_list

#麻雀牌の判定
def judgement(first,second):
    if first == second:
        return True
    else:False


if __name__ =='__main__':
    main()


