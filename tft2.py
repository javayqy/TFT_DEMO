# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

#寻找对局
def into_game():
    
    home_zaiwanyici_location = exists(Template(r"tpl1691746773783.png", record_pos=(0.134, 0.106), resolution=(1920, 1080)))

    #继续对局
    if home_zaiwanyici_location:
        print ("在大厅中")
        touch(Template(r"tpl1691746773783.png", record_pos=(0.134, 0.106), resolution=(1920, 1080)))
        
    sleep(2)

     #开启对局
    home_xunzhaoduiju_location = exists(Template(r"tpl1691740755175.png", record_pos=(0.205, 0.119), resolution=(1920, 1080)))
    if home_xunzhaoduiju_location :
        print ("在大厅中")
        touch(Template(r"tpl1691740755175.png", record_pos=(0.205, 0.119), resolution=(1920, 1080)))
    wait_jieshouduiju_click()
    
#自动play
def play_game():
    pic1 = exists(Template(r"tpl1691768217809.png", record_pos=(0.272, 0.198), resolution=(1920, 1080)))
    pic2 = exists(Template(r"tpl1691768302298.png", record_pos=(0.356, 0.221), resolution=(1920, 1080)))
#     if pic1:
#         touch(Template(r"tpl1691768217809.png", record_pos=(0.272, 0.198), resolution=(1920, 1080)))

    
#     if pic2 :
#         touch(Template(r"tpl1691768302298.png", record_pos=(0.356, 0.221), resolution=(1920, 1080)))
    if pic1  or pic2:
        touch(pic1 if pic1 else pic2)
        print("点击卡牌")
    buff = exists(Template(r"tpl1691767977612.png", record_pos=(0.108, -0.127), resolution=(1920, 1080)))

    if buff:
        touch(Template(r"tpl1691764133041.png", record_pos=(-0.158, -0.04), resolution=(1920, 1080)))
#     npc_move_templates = [Template(r"tpl1691767900359.png", record_pos=(0.352, 0.039), resolution=(1920, 1080)),Template(r"tpl1691768397271.png", record_pos=(0.113, -0.18), resolution=(1920, 1080)),Template(r"tpl1691768539559.png", record_pos=(0.025, 0.014), resolution=(1920, 1080))]
        
#     for templates in npc_move_templates:
#         if exists(templates):
#             touch(templates,right_click=True)
#             print("角色移动")

#     if npc_move1:
#         print("角色移动")
#         touch(Template(r"tpl1691767900359.png", record_pos=(0.352, 0.039), resolution=(1920, 1080)),right_click=True)
#     if npc_move2:
#         touch(Template(r"tpl1691768397271.png", record_pos=(0.113, -0.18), resolution=(1920, 1080)),right_click=True)
#     if npc_move3:
#         touch(Template(r"tpl1691768539559.png", record_pos=(0.025, 0.014), resolution=(1920, 1080)),right_click=True)
    print("没有爷想要的卡了")
    r_d = exists(Template(r"tpl1691764200760.png", record_pos=(-0.203, 0.206), resolution=(1920, 1080)))
    if r_d:
        print("DDDDD")
        touch(Template(r"tpl1691764200760.png", record_pos=(-0.203, 0.206), resolution=(1920, 1080)))
    up_level  = exists(Template(r"tpl1691764230599.png", record_pos=(-0.19, 0.173), resolution=(1920, 1080)))
    if up_level:
        touch(Template(r"tpl1691764230599.png", record_pos=(-0.19, 0.173), resolution=(1920, 1080)))
            

# 判断场景
def game_state():
    game_tag_location_1 = exists(Template(r"tpl1691745530077.png", record_pos=(0.045, -0.231), resolution=(1920, 1080)))

    home_tag_location = exists(Template(r"tpl1691746773783.png", record_pos=(0.134, 0.106), resolution=(1920, 1080)))
    home_tag_location2 = exists(Template(r"tpl1691765840915.png", record_pos=(0.115, -0.052), resolution=(1920, 1080)))


    find_location = None
    
    if game_tag_location_1:
        find_location = game_tag_location_1
        print('在游戏界面中 game_tag_location_1')
#     if game_tag_location_2:
#         find_location = game_tag_location_2
#         print('在游戏界面中 game_tag_location_2')

        
    if find_location:
        
        return 1   



    if home_tag_location or home_tag_location2:
        print('在游戏主界面中')
        return 3

#退出游戏
def exit_game():
    game_exit_location = exists(Template(r"tpl1691746645388.png", record_pos=(0.206, 0.043), resolution=(1920, 1080)))
    if game_exit_location:
        print('点击左键结束游戏')
        touch(Template(r"tpl1691746645388.png", record_pos=(0.206, 0.043), resolution=(1920, 1080)))
#接受对局
home_jieshouduiju_location =Template(r"tpl1691719700256.png", record_pos=(0.113, 0.189), resolution=(825, 576))
def wait_jieshouduiju_click():    
    i = 1
    while i<= 60 * 20:
#         home_jieshouduiju_location = exists(Template(r"tpl1691719700256.png", record_pos=(0.113, 0.189), resolution=(825, 576)))
        
        print(f'等待接受对局中... 已经等待{i}次')
#         wait(Template(r"tpl1691719700256.png", record_pos=(0.113, 0.189), resolution=(825, 576)),timeout = 60)
#         if home_jieshouduiju_location:
        if exists(home_jieshouduiju_location):
            touch(home_jieshouduiju_location)
            sleep(1.0)
            break
        else:
            sleep(1.0)
        
        i = i+1
        

    
while True:
    try:
        state = game_state()
        if state == 1:
            play_game()
            exit_game()
        elif state == 3:
            into_game()
        else:
            print("等待")
        sleep(2.0)
    except Exception as e:
        print('异常' + str(e))
