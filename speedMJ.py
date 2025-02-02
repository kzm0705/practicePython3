import PySimpleGUI as sg
import os
from random import choice, shuffle,sample

images =['manz (1).png', 'manz (2).png', 'manz (3).png', 'manz (4).png', 'manz (5).png', 'manz (6).png', 'manz (7).png',
          'piz (1).png', 'piz (10).png', 'piz (2).png', 'piz (3).png', 'piz (4).png', 'piz (5).png', 'piz (6).png', 'piz (7).png', 'piz (8).png', 'piz (9).png', 
         'souz (1).png', 'souz (10).png', 'souz (2).png', 'souz (3).png', 'souz (4).png', 'souz (5).png', 'souz (6).png', 'souz (7).png', 'souz (8).png', 'souz (9).png', 
         'tupai (1).png', 'tupai (2).png', 'tupai (3).png', 'tupai (4).png', 'tupai (5).png', 'tupai (6).png', 'tupai (7).png']

first,first_key = "",""
second = ""
count = 10
def main():
    global first, first_key, second, count
    random_hi = get_image(images)
    shuffle_hi = sample(random_hi, len(random_hi))
    shuffle_hi_2 = sample(random_hi, len(random_hi))

    layout = [[sg.Text('麻雀'),sg.Button('ランキング'),sg.Button('設定'),sg.Text(count,key='-count-')],
          [sg.Image(filename=path, key=f'row1{i}',enable_events=True, pad=((0,8),(100,10))) for i, path in enumerate(shuffle_hi[0:8])],
          [sg.Image(filename=path, key=f'row2{i}', enable_events=True, pad=((0,8),(8,10))) for i, path in enumerate(shuffle_hi[8:16])],
          [sg.Image(filename=path, key=f'row3{i}', enable_events=True,pad=((0,8),(8,10))) for i, path in enumerate(shuffle_hi_2[0:8])],
          [sg.Image(filename=path, key=f'row4{i}', enable_events=True,pad=((0,8),(8,10))) for i, path in enumerate(shuffle_hi_2[8:16])],
          ]

    window = sg.Window('麻雀スピード', layout, size=(600,600),element_justification='center')
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break
        #画像が押された処理
        if event.startswith('row'):
            if not first:
                first = window[event].Filename
                first_key=window[event].Key
                window[event].update(filename='.\\images\\tupai\\tupai (1).png', subsample=2)
            else:
                second = window[event].Filename
                count,second = check(first,second)
                window[first_key].update(filename=first)
                window['-count-'].update(count)
                first = ""

        #マウスの位置を取得
        x, y = window.mouse_location()

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
    for i in range(16):
        image = choice(seq)
        if image.startswith('m'):
            path =os.path.join('.\images\manz', image)
        elif image.startswith('p'):
            path =os.path.join('.\images\pins', image)
        elif image.startswith('s'):
            path = os.path.join('.\images\souz',image)
        else:path = os.path.join('.\\images\\tupai', image)
        path_list.append(path)
    return path_list

def check(first, second):
    global count
    if first == second:
        count -= 1
    return count, ""

if __name__ =="__main__":

    main()