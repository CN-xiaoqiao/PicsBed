"""
@author: Jim
@project: PicsBed
@file: pypcrypt.py
@time: 2020/5/23 13:21
@desc:  

    加密模块，使用AES的CBC模式
"""

from binascii import b2a_base64, a2b_base64

from Crypto.Cipher import AES

from typing import Union


class Pypcrypt:
    """
        使用AES 的加密解密
    """
    def __init__(self, key):
        """
        Args:
            key: 对称加密的key
        """
        self.mode = AES.MODE_CBC
        self.key = self.pad(key)

    def pad(self, text: Union[str, bytes]):
        """
            将text字符串转成bytes类型，并且凑成16位长度
        Args:
            text:

        Returns:

        """
        if isinstance(text, str):
            text = bytes(text, encoding="utf8")

        while len(text) % 16 != 0:
            text += b'\0'
        return text

    def encrypt(self, text: str):
        """
            加密
        Args:
            text:

        Returns:

        """
        texts = self.pad(text)
        aes = AES.new(self.key, self.mode, self.key)
        res = aes.encrypt(texts)
        return str(b2a_base64(res), encoding="utf-8")

    def decrypt(self, text):
        """
            解密
        Args:
            text:

        Returns:

        """
        texts = a2b_base64(self.pad(text))
        aes = AES.new(self.key, self.mode, self.key)
        res = str(aes.decrypt(texts), encoding="utf8")
        return res


if __name__ == '__main__':
    pcrypt = Pypcrypt("abcdefg")
    rst = pcrypt.encrypt("zhangsan")
    # print(rst)
    # rst = pcrypt.decrypt("km85zlzsaEZRrDg0X7nhmA==")
    # print(rst)
