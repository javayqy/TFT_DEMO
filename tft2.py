# -*- encoding=utf8 -*-
__author__ = "Administrator"
import time
from airtest.core.api import *

auto_setup(__file__)

#寻找对局
def into_game():
    
    home_zaiwanyici_location = exists(Template(r"tpl1691746773783.png", record_pos=(0.134, 0.106), resolution=(1920, 1080)))

    #继续对局
    if home_zaiwanyici_location:
        print ("点击再玩一次")
        touch(Template(r"tpl1691746773783.png", record_pos=(0.134, 0.106), resolution=(1920, 1080)))
        
        sleep(3)

     #开启对局
    home_xunzhaoduiju_location = exists(Template(r"tpl1691740755175.png", record_pos=(0.205, 0.119), resolution=(1920, 1080)))
    if home_xunzhaoduiju_location :
        print ("点击寻找对局")
        touch(Template(r"tpl1691740755175.png", record_pos=(0.205, 0.119), resolution=(1920, 1080)))
        wait_jieshouduiju_click()
    
    
#自动play
def play_game():
    pic1 = exists(Template(r"tpl1691768217809.png", record_pos=(0.272, 0.198), resolution=(1920, 1080)))
    pic2 = exists(Template(r"tpl1691768302298.png", record_pos=(0.356, 0.221), resolution=(1920, 1080)))
    if pic1:
        touch(Template(r"tpl1691768217809.png", record_pos=(0.272, 0.198), resolution=(1920, 1080)))
    if pic2 :
        touch(Template(r"tpl1691768302298.png", record_pos=(0.356, 0.221), resolution=(1920, 1080)))
    if pic1 or pic2:
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
#     up_level  = exists(Template(r"tpl1691764230599.png", record_pos=(-0.19, 0.173), resolution=(1920, 1080)))
#     if up_level:
#         touch(Template(r"tpl1691764230599.png", record_pos=(-0.19, 0.173), resolution=(1920, 1080)))
            

# 判断场景
def game_state():
    game_tag_location_1 =exists(Template(r"tpl1691847051087.png", record_pos=(-0.103, -0.009), resolution=(1920, 1080)))


    home_tag_location2 = exists(Template(r"tpl1691834533639.png", record_pos=(0.201, -0.043), resolution=(1920, 1080)))


    home_tag_location3 = exists(Template(r"tpl1691746773783.png", record_pos=(0.134, 0.106), resolution=(1920, 1080)))
    
    find_location = None
    
    if game_tag_location_1:
        find_location = game_tag_location_1
        print('在游戏中 ')
    if find_location:    
        return 1   
    if home_tag_location2 or home_tag_location3:
        print('在主界面中')
        return 2

#退出游戏
def exit_game():
    game_exit_location = exists(Template(r"tpl1691746645388.png", record_pos=(0.206, 0.043), resolution=(1920, 1080)))
    if game_exit_location:
        print('点击左键结束游戏')
        touch(Template(r"tpl1691746645388.png", record_pos=(0.206, 0.043), resolution=(1920, 1080)))
        
#接受对局

def wait_jieshouduiju_click():  
    home_jieshouduiju_location =Template(r"tpl1691719700256.png", record_pos=(0.113, 0.189), resolution=(825, 576))
    i = 1
    ingame = Template(r"tpl1691847051087.png", record_pos=(-0.103, -0.009), resolution=(1920, 1080))
    while i<= 200 and ingame:      
        print(f'等待接受对局中... 已经等待{i}次')
        if exists(home_jieshouduiju_location):
            touch(home_jieshouduiju_location)
        i = i+1
        if exists(ingame):
            print('进入游戏了')
            break

last_game_check_time = 0    
in_game = False

while True:
    try:
        current_time = time.time()
        
        # 如果在游戏中且不超过一分钟，连续执行 play_game() 和 exit_game()
        if in_game and current_time - last_game_check_time <= 60:
            play_game()
            exit_game()
            
        # 如果不在游戏中或超过一分钟，执行游戏状态检测和操作
        else:
            state = game_state()
            if state == 1:
                in_game = True
                play_game()
                exit_game()
                last_game_check_time = current_time
            elif state == 2:
                into_game()
                in_game = False
                last_game_check_time = current_time
            
        sleep(1.0)
    except Exception as e:
        print('异常' + str(e))
#     exists(Template(r"tpl1691847860790.png", record_pos=(0.018, 0.21), resolution=(1920, 1080)))
#     exists(Template(r"tpl1691847911203.png", record_pos=(0.017, 0.216), resolution=(1920, 1080)))
# exists(Template(r"tpl1691848009122.png", record_pos=(0.366, 0.186), resolution=(1920, 1080)))exists(Template(r"tpl1691848047192.png", record_pos=(0.366, 0.188), resolution=(1920, 1080)))
# exists(Template(r"tpl1691848065712.png", record_pos=(0.279, 0.187), resolution=(1920, 1080)))exists(Template(r"tpl1691848164975.png", record_pos=(0.017, 0.186), resolution=(1920, 1080)))exists(Template(r"tpl1691848292909.png", record_pos=(0.017, 0.185), resolution=(1920, 1080)))exists(Template(r"tpl1691848321475.png", record_pos=(0.367, 0.186), resolution=(1920, 1080)))
# exists(Template(r"tpl1691848356021.png", record_pos=(0.018, 0.186), resolution=(1920, 1080)))






