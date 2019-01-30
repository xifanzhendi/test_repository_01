# coding : utf-8
import unittest
import os
from commen import HTMLTestRunner
# 查找用例的文件夹 绝对路径

# 代码涉及路径地方不要写死，不利于移植

# start_dir = r"E:\apiproject\cases"


curpath = os.path.dirname(os.path.realpath(__file__)) # 获取当前脚本的完整路径
print(curpath)
casepath = os.path.join(curpath,"cases") #拼接路径
print(casepath)

pattern="test*.py"  # 匹配规则
discover = unittest.defaultTestLoader.discover(casepath,pattern)
print(discover)

# runner = unittest.TextTestRunner()
# runner.run(discover)

reportpath = os.path.join(curpath,"report","report.html")
fp = open(reportpath,"wb")   # 打开 report路径 ,wb二进制写入
runner =  HTMLTestRunner.HTMLTestRunner(stream=fp,
                                        title="接口测试用例报告",
                                        description="测试用例详情描述")

runner.run(discover)