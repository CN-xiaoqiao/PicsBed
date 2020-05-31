"""
@author: Jim
@project: PicsBed
@file: picture.py
@time: 2020/5/30 16:22
@desc:  
    
"""

from utils.exts import db


class Picture(db.Document):
    name = db.StringField()
    real_name = db.StringField()
    uid = db.IntField()
    source = db.StringField()
    create_time = db.IntField()
