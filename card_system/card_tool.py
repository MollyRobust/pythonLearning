#!/usr/bin/env python
# encoding: utf-8

# 名片集合-存放所有名片字典
name_list = []

def guide_word():
    print("*"*50)
    print("1-新建名片\n2-查看全部名片\n3-查询名片\n\n0-退出系统")
    print("*"*50)


def set_card():
    """
    新建名片功能
    """
    # 名片字典存放个人信息
    name_dict = dict()
    name_dict["name"] = input("name:")
    name_dict["phone"] = input("phone:")
    name_dict["qq"] = input("qq:")
    name_dict["email"] = input("email:")
    name_list.append(name_dict)


def get_all_cards():
    """
    显示全部名片
    """
    # 打印表头
    print("="*50)
    print("姓名\t\t电话\t\tqq\t\t邮箱\t\t")
    print("-" * 50)
    # 循环查看name_list中的所有名片字典
    for name_dict in name_list:
        name_str = name_dict["name"]
        phone_str = name_dict["phone"]
        qq_str = name_dict["qq"]
        email_str = name_dict["email"]
        print("%s\t\t%s\t\t%s\t\t%s"%(name_str, phone_str, qq_str, email_str))
    print("=" * 50)
    print("查询完毕\n\n\n")


def get_one_card(name_str):
    # 在name_list中循环查找姓名
    for name_dict in name_list:
        if name_str == name_dict["name"]:
            print("姓名\t\t电话\t\tqq\t\t邮箱\t\t")
            print("-" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (name_str, name_dict["phone"], name_dict["qq"], name_dict["email"]))
            break
    else:
        print("抱歉，名片系统中没有您要查询的姓名！")

