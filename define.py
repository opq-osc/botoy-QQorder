# -*- coding:utf-8 -*-
# 用户：HYL
# 日期：2021年11月19日
import json

# -------------指令管理-------------------
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

# ---------日记本功能-----------------
def jiancha(qq_num):
    with open('日记.json', 'r+', encoding='utf-8') as f:
        dic = json.load(f)
    if f"{qq_num}" not in dic:
        flag = False  # 对象不存在
    else:
        flag = True
    return flag


def chuangjian(qq_num):
    if not jiancha(qq_num):
        with open('日记.json', 'r+', encoding='utf-8') as f:
            dic = json.load(f)
        with open('日记.json', 'w+', encoding='utf-8') as f:
            dic[f"{qq_num}"] = {}
            json.dump(dic, f)
        return "日记本创建成功，快去写日记吧！"
    else:
        return "你已经了创建日记本，快去写日记吧！"


def chakan(qq_num):
    if jiancha(qq_num):
        with open('日记.json', 'r+', encoding='utf-8') as f:
            dic = json.load(f)
        my_dic = dic[f"{qq_num}"]
        content = ''
        if my_dic:
            for k, v in my_dic.items():
                content += k + ':' + v + '\n' + '\n'
        if content == '':
            return "日记为空"
        else:
            return content
    else:
        return "日记查看失败，请先创建日记本！"


def xieriji(content, title, qq_num):
    if jiancha(qq_num):
        with open('日记.json', 'r+', encoding='utf-8') as f:
            dic = json.load(f)
        with open('日记.json', 'w+', encoding='utf-8') as f:
            dic[f"{qq_num}"][f"{title}"] = "记录时间为:\n" + str(datetime.datetime.now()) + "\n" + content
            json.dump(dic, f)
        return "日记已记录！"
    else:
        return "日记记录失败，请先创建日记本！"


def shanchu(title, qq_num):
    if jiancha(qq_num):
        with open('日记.json', 'r+', encoding='utf-8') as f:
            dic = json.load(f)
            if title in dic[f"{qq_num}"]:
                with open('日记.json', 'w+', encoding='utf-8') as f:
                    dic[f"{qq_num}"].pop(f"{title}")
                    json.dump(dic, f)
                return "日记删除成功！"
            else:
                return "无此日记，请检查日记标题"

    else:
        return "日记删除失败，请先创建日记本！"


#  ------------------------------------------------------

