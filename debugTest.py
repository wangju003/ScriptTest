import os

from case.Region.test_data_repeat import RegionDataTest
from common.run_case_util import RunModle
case_path = os.path.join(os.path.abspath("."), "case")


run_modle=RunModle()

if __name__ == "__main__":
#     #执行case目录下全部测试用例
#     # run_modle.run_all_case(case_path)

#     #执行case目录下 Region目录下，所有测试文件中的测试用例
#     run_modle.run_all_case_for_a_class(RegionDataTest)

    # 执行case目录下 Region目录下，所有测试文件中指定的一个测试用例
#     run_modle.run_single_case_for_a_class(RegionDataTest,'test_region_repeat')

    caseList=[RegionDataTest("test_region_repeat"),RegionDataTest("test_square_repeat")]
    run_modle.run_few_case_for_many_class(caseList)

