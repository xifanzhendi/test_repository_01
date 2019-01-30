# coding : utf-8
import unittest
import requests
class Test_QQ(unittest.TestCase):
    def test_02(self):
        '''key错误的是时候xxx'''
        url = "http://japi.juhe.cn/qqevaluate/qq"
        par = {

                "key": "e94efe0eb5ae630a708435fbe1ce7fb1",
                "qq": "7296522XX"
            }
        r = requests.get(url, params=par)
        res = r.json()
        print(res) # json转字典
        self.assertTrue(res["reason"] == "错误的请求参数")