import  unittest

class GetCase(object):
    '''
    按指定的方式组织测试用例
    '''

    def get_all_case(self,case_path):
        '''
        运行指定目录下的全部测试用例
        :param case_path: str
        :return:None
        '''

        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
        return discover

    def get_all_case_for_a_class(self,className):
        '''
        测试一个测试类中所有的测试用例
        :param className: 测试类名 obj
        :return:suite
        '''
        suite = unittest.makeSuite(className, 'test')
        return suite

    def get_single_case_for_a_class(self,className, caseName):
        '''
        指定1个测试类中的1个测试用例
        :param className: 测试类名 obj
        :param caseName: 指定要运行的1个测试用例名称 str
        :return:
        '''
        suite = unittest.TestSuite()
        suite.addTest(className(caseName))
        return suite

    def get_few_case_for_many_class(self,caseList):
        '''
        指定任意测试类，任意测试用例
        :param caseList: 测试用例list[测试类名（'测试用例名'）]，示例caseList = [AcBroker("test_login"), AcBroker('test_loginout'), AcBroker('test_checkedition')]
        :return:
        '''
        suite = unittest.TestSuite()
        suite.addTests(caseList)
        return suite

class RunModle(object):
    '''
    指定case运行模式
    '''
    def __init__(self):
        self.get_case = GetCase()
        self.runner=unittest.TextTestRunner()
    def run_all_case(self,case_path):
        '''
        执行指定路径下的全部测试用例
        :param case_path:
        :return:None
        '''
        self.runner.run(self.get_case.get_all_case(case_path))
    def run_all_case_for_a_class(self,className):
        self.runner.run(self.get_case.get_all_case_for_a_class(className))
    def run_single_case_for_a_class(self,className,caseName):
        self.runner.run(self.get_case.get_single_case_for_a_class(className,caseName))
    def run_few_case_for_many_class(self,caseList):
        self.runner.run(self.get_case.get_few_case_for_many_class(caseList))
