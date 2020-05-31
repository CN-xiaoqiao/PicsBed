"""
@author: Jim
@project: PicsBed
@file: alioss.py
@time: 2020/5/30 11:07
@desc:  
"""

import oss2
from models.user import User


class AliOss:

    def __init__(self, username: str):
        self.__username = username
        self.__init_conn()

    def __init_conn(self):
        """
            初始化连接
        Returns:

        """
        user = User.objects(username=self.__username).fields(source={'$elemMatch': {'enable': True}}).first()
        source = user.source[0]
        access_key = source.access_key
        access_key_secert = source.access_key_secert
        endpoint = source.endpoint
        bucket = source.bucket

        self.__path = source.path

        self.auth(access_key, access_key_secert)
        self.select_bucket(endpoint, bucket)

    def auth(self, access_key: str, access_key_secert: str):
        """
            连接
        Args:
            access_key:
            access_key_secert:

        Returns:

        """
        self.__auth = oss2.Auth(access_key, access_key_secert)

    def select_bucket(self, endpoint: str, bucket: str):
        """

        Args:
            endpoint:
            bucket:

        Returns:

        """
        self.__bucket = oss2.Bucket(self.__auth, endpoint, bucket)

    def upload_from_bytes(self, src_file: bytes, to_file: str):
        """
            上传文件
        Args:
            src_file: 需要保存的图片二进制文件
            to_file: 文件名

        Returns:

        """

        file_path = "{}/{}".format(self.__path, to_file)
        ret = self.__bucket.put_object(file_path, src_file)
        if ret.status == 200:
            return True


if __name__ == '__main__':
    oss = AliOss()

    with open("Image.jpg", "rb") as f:
        ret = oss.upload(None, f, "test2.jpg")
        print(ret)
