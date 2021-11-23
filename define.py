# -*- coding:utf-8 -*-
# 用户：HYL
# 日期：2021年11月19日
import json


# 读取对话
def dialog():
    with open('对话.json', 'r+') as file:
        dic = json.load(file)
        return dic


# 定义指令
def define(a, b):
    new_dic = dialog()
    with open('对话.json', 'w+') as file:
        new_dic[a] = b
        json.dump(new_dic, file)


# 查看指令
def look_up():
    look = ''
    for k, v in dialog().items():
        look += k + ':' + v + '\n' + '\n'
    return look


# 指令删除
def delete(a):
    new_dic = dialog()
    if a in new_dic:
        with open('对话.json', 'w+') as file:
            del new_dic[a]
            json.dump(new_dic, file)
        return True
    else:
        return False
