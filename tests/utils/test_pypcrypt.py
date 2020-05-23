"""
@author: Jim
@project: PicsBed
@file: test_pypcrypt.py
@time: 2020/5/23 13:35
@desc:  
    
"""

from PicsBed.utils.pypcrypt import Pypcrypt


class TestPypcrypt:

    def setup_class(self):
        self.pcrypt = Pypcrypt("abcdefg")

    def test_encrypt(self):
        rst = self.pcrypt.encrypt("zhangsan")
        assert rst.strip() == "km85zlzsaEZRrDg0X7nhmA=="

    def test_decrypt(self):
        rst = self.pcrypt.decrypt("km85zlzsaEZRrDg0X7nhmA==")
        print(rst)
        assert rst.strip() == "zhangsan"
