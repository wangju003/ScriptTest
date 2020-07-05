import os

from common.run_case_util import RunModle
case_path = os.path.join(os.path.abspath("."), "case")


run_modle=RunModle()

if __name__ == "__main__":
#     #执行case目录下全部测试用例
    run_modle.run_all_case(case_path)


