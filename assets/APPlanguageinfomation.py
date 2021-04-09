# -*- encoding:utf-8 -*-


import os
import sys


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        #base_path = os.path.abspath(".")
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)


#filename = resource_path(os.path.join("assets", "help.html"))
filename = resource_path(os.path.join("help.html"))
winIcon_path = resource_path(os.path.join("testTools.ico"))

def read_html():
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
    return content


class messageInfor:
    def __init__(self):
        pass

    about_infor = "当前版本： v 1.0.0"
    help_infor = read_html()
    windowIcon = winIcon_path
