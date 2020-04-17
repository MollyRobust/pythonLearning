#!/usr/bin/env python
# encoding: utf-8
import card_tool
# 名片系统
welcome_word = "欢迎使用名片管理系统"

# 判断输入的内容：1-新建名片 2-查看全部名片 3-查询名片 0-退出系统
while True:
    card_tool.guide_word()
    # 输入操作
    action_id = input("请输入您要进行的操作:")
    if action_id in ("1", "2", "3"):
        # 进行对应操作
        # print("进行相关操作")
        if action_id == "1":
            # 新建名片
            card_tool.set_card()
        elif action_id == "2":
            # 查看全部名片
            card_tool.get_all_cards()
        else:
            # 查询指定姓名名片
            name_str = input("请输入您要查询的姓名：")
            card_tool.get_one_card(name_str)
    elif action_id == "0":
        # 退出系统，结束循环
        break
    else:
        # 其他输入都是非法输入，给出提示
        print("您的输入有误，请重新输入")