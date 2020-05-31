"""
@author: Jim
@project: PicsBed
@file: user.py
@time: 2020/5/30 16:22
@desc:  
    
"""

from utils.exts import db


class Source(db.EmbeddedDocument):
    name = db.StringField()
    where = db.StringField()
    real_name = db.StringField()
    path = db.StringField()
    access_key = db.StringField()
    access_key_secert = db.StringField()
    endpoint = db.StringField()
    bucket = db.StringField()
    enable = db.BooleanField()


class User(db.Document):
    username = db.StringField()
    password = db.StringField()
    email = db.StringField()
    phone = db.StringField()
    source = db.ListField(db.EmbeddedDocumentField(Source))
    create_time = db.IntField()
    update_time = db.IntField()
