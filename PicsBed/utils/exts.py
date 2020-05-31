"""
@author: Jim
@project: PicsBed
@file: exts.py
@time: 2020/5/30 17:42
@desc:  
    插件
"""

from flask_mongoengine import MongoEngine
from flask import Flask

db = MongoEngine()


def init_app(app: Flask):
    db.init_app(app)
