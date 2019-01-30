# coding : utf-8
import unittest
import requests
import time
class Test_QQ(unittest.TestCase):
    def test_01(self):
        '''key正确e94efe0eb5ae630a708435fbe1ce7fb1'''
        time.sleep(2)
        url = "http://japi.juhe.cn/qqevaluate/qq"
        par = {

            "key": "e94efe0eb5ae630a708435fbe1ce7fb1",
            "qq": "729652227"
        }
        r = requests.get(url, params=par)
        res = r.json()
        print(res) # json转字典
        # 所有测试结果判断，都可以用True和False来判定


        #实际结果 ，把实际结果取出来

        #期望结果

        # 断言  实际结果和期望结果
        # self.assertTrue(res["reason"] == "success")
        # self.assertTrue(res["error_code"]== 0)
        self.assertTrue(res["reason"] == "success" or res["error_code"]== 0 ) # 断言实际结果和期望结果满足一个就可以，都是and


        # if res["reason"] == 'success':
        #     print("测试通过")
        # else:
        #     print("测试失败")
    def test_02(self):
        '''key错误的是时候xxx'''
        url = "http://japi.juhe.cn/qqevaluate/qq"
        par = {

                "key": "e94efe0eb5ae630a708435fbe1ce7fb1",
                "qq": "729652227"
            }
        r = requests.get(url, params=par)
        res = r.json()
        print(res) # json转字典
        self.assertTrue(res["reason"] == "错误的请求参数")



if __name__ == "__main__":
    unittest.main()
