import unittest
import os

from case.demo import *

case_path = os.path.join(os.path.abspath("."), "case")
print(case_path)

# 组织测试用例
def addSuite(caseList):
    suite = unittest.TestSuite()
    suite.addTests(caseList)
    return suite


# 执行全部测试用例 并生成测试报告　
def call_case():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    return discover



if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(call_case())

