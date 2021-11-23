# -*- coding:utf-8 -*-
# 用户：HYL
# 日期：2021年10月21日
from botoy import Botoy, GroupMsg, Action, FriendMsg, decorators
from define import *


qq = 123456
bot = Botoy(qq=qq)
action = Action(qq=qq)


@bot.on_group_msg
@decorators.ignore_botself
def zhi_ling(ctx: GroupMsg):
    if ctx.Content in dialog():
        result = dialog()[ctx.Content]
        action.sendGroupText(ctx.FromGroupId, result)
        # 指令管理
    elif ctx.Content[0:4] == '定义指令' and len(ctx.Content) > 4:
        try:
            after = ctx.Content.split(' ', 2)
            define(after[1], after[2])
            result = '指令定义成功'
            action.sendGroupText(ctx.FromGroupId, result)
        except BaseException:
            result = '指令添加失败，请检查格式'
            action.sendGroupText(ctx.FromGroupId, result)
    elif ctx.Content == '查看指令':
        result = look_up()
        action.sendGroupText(ctx.FromGroupId, result)
    elif ctx.Content[0:4] == '删除指令' and len(ctx.Content) > 4:
        after = ctx.Content.split(' ', 1)
        flag = delete(after[1])
        if flag:
            result = '指令删除成功'
            action.sendGroupText(ctx.FromGroupId, result)
        else:
            result = '指令删除失败，格式错误或者无该指令'
            action.sendGroupText(ctx.FromGroupId, result)


if __name__ == '__main__':
    bot.run()