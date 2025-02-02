import PySimpleGUI as sg
import os
from random import choice, shuffle,sample
from datetime import timedelta,datetime
import time

images =['manz (1).png', 'manz (2).png', 'manz (3).png', 'manz (4).png', 'manz (5).png', 'manz (6).png', 'manz (7).png',
          'piz (1).png', 'piz (10).png', 'piz (2).png', 'piz (3).png', 'piz (4).png', 'piz (5).png', 'piz (6).png', 'piz (7).png', 'piz (8).png', 'piz (9).png', 
         'souz (1).png', 'souz (10).png', 'souz (2).png', 'souz (3).png', 'souz (4).png', 'souz (5).png', 'souz (6).png', 'souz (7).png', 'souz (8).png', 'souz (9).png', 
         'tupai (1).png', 'tupai (2).png', 'tupai (3).png', 'tupai (4).png', 'tupai (5).png', 'tupai (6).png', 'tupai (7).png']

first,first_key = "",""
second = ""
count = 0
countdown = 3
elapsed_time =timedelta(0)
running = True

def main():
    global first, first_key, second, count,running
    random_hi = get_image(images)
    shuffle_hi = sample(random_hi, len(random_hi))
    shuffle_hi_2 = sample(random_hi, len(random_hi))
    start_time = datetime.now()

    layout = [[sg.Text('麻雀',font=('Helvetica', 20) ,pad=((200,0),(20,0))),sg.Button('ランキング',pad=((80,0),(20,0))),sg.Text('0:00:00:00', key='-timer-',pad=((30,0),(20,0)))],
              [sg.Button('newgame',key='new',pad=((0,50),(30,0))),sg.Button('start',key='-start-', size=(8,1),pad=((50,0),(30,0))),sg.Text(3,key='countdown', font=('Helvetica', 20),text_color='black',pad=((200,0),(30,0)))],
          [sg.Image(filename=path, key=f'row1{i}',enable_events=True, pad=((0,8),(60,10)),) for i, path in enumerate(shuffle_hi[0:8])],
          [sg.Image(filename=path, key=f'row2{i}', enable_events=True, pad=((0,8),(8,10))) for i, path in enumerate(shuffle_hi[8:16])],
          [sg.Image(filename=path, key=f'row3{i}', enable_events=True,pad=((0,8),(8,10))) for i, path in enumerate(shuffle_hi_2[0:8])],
          [sg.Image(filename=path, key=f'row4{i}', enable_events=True,pad=((0,8),(8,10)),) for i, path in enumerate(shuffle_hi_2[8:16])],
          ]

    window = sg.Window('麻雀スピード', layout, size=(600,600),element_justification='center')
    while True:
        event, values = window.read(timeout=30)

        if event == sg.WINDOW_CLOSED:
            break
        #画像が押された処理
        if event.startswith('row'):
            #一枚目選択時
            if not first:
                first = window[event].Filename
                first_key=window[event].Key
                window[event].update(filename='.\\images\\tupai\\tupai (1).png', subsample=2)
            #二枚目選択時
            else:
                second = window[event].Filename
                count, second, result = check(first,second)
                if result:
                    window[first_key].update("")
                    window[event].update("")
                    first = ""
                else:
                    window[first_key].update(filename=first)
                    first = ""
#スタートボタンを押したとき
        if event =='-start-':
            window['-start-'].update(disabled=True)
            countdown = 3
            for i in range(3):
                countdown -= 1
                time.sleep(1)
                window['countdown'].update(str(countdown))
            start_time = datetime.now()
            count = 16
            
        #タイマーの処理
        if count != 0:
            current_time = datetime.now() - start_time + elapsed_time
            window['-timer-'].update(str(current_time)[:-4])
        else:pass

    window.close()

#ディレクトリ走査
def mk_image_list(dir:str):
    images = []
    for root ,dirs,files in os.walk(dir):
        for file in files:
            images.append(file)
    return images

def get_image(seq):
    path_list = []
    sampled = sample(seq, 16)
    for card in sampled:
        if card.startswith('m'):
            path =os.path.join('.\images\manz', card)
        elif card.startswith('p'):
            path =os.path.join('.\images\pins', card)
        elif card.startswith('s'):
            path = os.path.join('.\images\souz',card)
        else:path = os.path.join('.\\images\\tupai', card)
        path_list.append(path)
    return path_list

#麻雀牌のチェック
def check(first, second):
    global count
    if first == second:
        count -= 1
        return count, "", True
    else:return count,"", False

def save_time(score_time):
    with open('score_time.txt','w',encoding='utf-8') as f:
        f.write(score_time)
    sg.popup('ランキング更新しました')

def countdown():
    for i in range(3):
        count -= 1
        time.sleep(1)
        return count
        


if __name__ =="__main__":

    main()