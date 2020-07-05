import  requests
import unittest
from common.assert_util import assert_repeat
from common.util import logging
from common.util import param_city_url

class RegionDataTest(unittest.TestCase):
    '''
    区域商圈数据是否重复
    '''
    base_url = 'https://appapi.5i5j.com/appapi/region/{city_id}/v1/list'

    @param_city_url(base_url)
    def test_region_repeat(self,base_url):
        data = {}
        r = requests.post(base_url, data)
        res_data = r.json()['data']
        # res_data=test_data
        region_names= [i['name'] for i in res_data]
        is_repeat = assert_repeat(region_names)

        if is_repeat:
            logging.error('区域商圈 顶级区域重复，请人工核验! %s'%base_url)

    @param_city_url(base_url)
    def test_square_repeat(self,base_url):
        data = {}
        r = requests.post(base_url, data)
        res_data = r.json()['data']
        for i in res_data:
            region_name = i['name']
            square_name_data = i['sqlist']

            square_names = [j['name'] for j in square_name_data]
            is_repeat = assert_repeat( square_names)
            if is_repeat:
                logging.error('区域商圈 子区块重复! 请人工核验 %s区 二级区块！' % region_name)

if __name__ =='__main__':
    unittest.main()