"""
@author: Jim
@project: PicsBed
@file: image.py
@time: 2020/5/30 16:01
@desc:  
    
"""
import os
import uuid

from flask import views, request
from flask.blueprints import Blueprint
from werkzeug.utils import secure_filename

from utils.yun.alioss import AliOss

bp = Blueprint("image", __name__, url_prefix="/image")


class UploadImageView(views.MethodView):

    def allowed_file(self, filename: str) -> bool:
        """
            检验扩展名. 判断文件是否上传
        Returns:

        """
        ALLOWED_EXTENSIONS = ["jpg", "png", "gif", "bmp"]

        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def post(self):
        """
            上传图片.
        Returns:
            外链
        """

        upload_img = request.files.get("upload_image", None)

        if upload_img and self.allowed_file(upload_img.filename):
            file_name = secure_filename(upload_img.filename)
            fake_name = "{}{}".format(uuid.uuid4().hex, os.path.splitext(file_name)[-1])

            alioss = AliOss("jim")
            if alioss.upload_from_bytes(upload_img, fake_name):
                return "ok"

        return "failed"


bp.add_url_rule("/upload", view_func=UploadImageView.as_view('upload'))
