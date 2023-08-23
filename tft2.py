# -*- encoding=utf8 -*-
__author__ = "Administrator"
import time
import threading
from airtest.core.api import *

auto_setup(__file__)

#寻找对局
def into_game():
    
    home_zaiwanyici_location = exists(Template(r"tpl1691746773783.png", record_pos=(0.134, 0.106), resolution=(1920, 1080)))

    #继续对局
    if home_zaiwanyici_location:
        print ("点击再玩一次")
        touch(Template(r"tpl1691746773783.png", record_pos=(0.134, 0.106), resolution=(1920, 1080)))
        
        sleep(10)

     #开启对局
    home_xunzhaoduiju_location = exists(Template(r"tpl1691740755175.png", record_pos=(0.205, 0.119), resolution=(1920, 1080)))
    if home_xunzhaoduiju_location :
        print ("点击寻找对局")
        touch(Template(r"tpl1691740755175.png", record_pos=(0.205, 0.119), resolution=(1920, 1080)))
        wait_jieshouduiju_click()
    #跳过等待
    home_tiaoguodengdai_location=exists(Template(r"tpl1692062153755.png", record_pos=(-0.018, 0.046), resolution=(1920, 1080)))
    if home_tiaoguodengdai_location:
        touch(home_tiaoguodengdai_location)
        sleep(5)
        touch(Template(r"tpl1692062610930.png", record_pos=(-0.035, -0.183), resolution=(1920, 1080)))
        touch(Template(r"tpl1692062647514.png", record_pos=(0.173, -0.066), resolution=(1920, 1080)))
        touch(Template(r"tpl1692062673090.png", record_pos=(0.138, 0.086), resolution=(1920, 1080)))
        wait(Template(r"tpl1692062720599.png", record_pos=(0.133, 0.083), resolution=(1920, 1080)))
        into_game()
        


    
    
#自动play
def play_game():

    pic_templates = [Template(r"tpl1691768217809.png", record_pos=(0.272, 0.198), resolution=(1920, 1080)),Template(r"tpl1691768302298.png", record_pos=(0.356, 0.221), resolution=(1920, 1080))]
    for piclist in pic_templates:
        if exists(piclist):
            touch(piclist)
            print("购买卡牌")
#             break
    buff = exists(Template(r"tpl1691767977612.png", record_pos=(0.108, -0.127), resolution=(1920, 1080)))
    if buff:
        touch(Template(r"tpl1691764133041.png", record_pos=(-0.158, -0.04), resolution=(1920, 1080)))
        print("获得buff")
    npc_move_templates = [Template(r"tpl1691767900359.png", record_pos=(0.352, 0.039), resolution=(1920, 1080)),Template(r"tpl1691768397271.png", record_pos=(0.113, -0.18), resolution=(1920, 1080)),Template(r"tpl1691768539559.png", record_pos=(0.025, 0.014), resolution=(1920, 1080))]
        
    for templates in npc_move_templates:
        if exists(templates):
            touch(templates,right_click=True)
            print("角色移动")
        else:
            print("没有找到可移动的位置")


    r_d = exists(Template(r"tpl1691764200760.png", record_pos=(-0.203, 0.206), resolution=(1920, 1080)))
    if r_d:
        print("刷新卡牌")
        touch(Template(r"tpl1691764200760.png", record_pos=(-0.203, 0.206), resolution=(1920, 1080)))
    up_level  = exists(Template(r"tpl1691764230599.png", record_pos=(-0.19, 0.173), resolution=(1920, 1080)))
    if up_level:
        touch(Template(r"tpl1691764230599.png", record_pos=(-0.19, 0.173), resolution=(1920, 1080)))
            

# 判断场景
def game_state():
    game_tag_location_1 =exists(Template(r"tpl1691847051087.png", record_pos=(-0.103, -0.009), resolution=(1920, 1080)))


    home_tag_location2 = exists(Template(r"tpl1691834533639.png", record_pos=(0.201, -0.043), resolution=(1920, 1080)))


    home_tag_location3 = exists(Template(r"tpl1691746773783.png", record_pos=(0.134, 0.106), resolution=(1920, 1080)))
    

    
    if game_tag_location_1:

        print('在游戏中 ')
        return 1 
          
    elif home_tag_location2 or home_tag_location3:
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
    home_xunzhaoduiju_location = Template(r"tpl1691740755175.png", record_pos=(0.205, 0.119), resolution=(1920, 1080))
    home_jieshouduiju_location =Template(r"tpl1691719700256.png", record_pos=(0.113, 0.189), resolution=(825, 576))
    i = 1
    ingame = Template(r"tpl1691847051087.png", record_pos=(-0.103, -0.009), resolution=(1920, 1080))
    while i<= 200 or ingame:      
        print(f'等待接受对局中... 已经等待{i}次')
        if exists(home_jieshouduiju_location):
            touch(home_jieshouduiju_location)
        elif exists(home_xunzhaoduiju_location):
            into_game()
        elif exists(ingame):
            print('进入游戏了')
            break
        else:
            i = i+1
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
        
#多线程(有点问题)
# def play_game_task():
#     while True:
#         state = game_state()
#         if state == 1:
#             play_game()
#             exit_game()
# def game_state_task():
#     while True:
#         state = game_state()
# #         if state == 1:
# # #             play_game()
# # #             exit_game()
#         if state == 2:
#             into_game()            
#             sleep(30.0)

# if __name__ == "__main__":
#     # 初始化必要的变量...

#     play_thread = threading.Thread(target=play_game_task)
#     state_thread = threading.Thread(target=game_state_task)

#     play_thread.start()
#     state_thread.start()

#     try:
#         while True:
#             time.sleep(1.0)
#     except KeyboardInterrupt:
#         play_thread.join()
#         state_thread.join()



# 