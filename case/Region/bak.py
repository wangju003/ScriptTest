import  requests
import unittest
from assert_util import assert_repeat
from util import logging
from parameterized import parameterized, param

#生成测试数据字典
from settings import citys
base_url='https://appapi.5i5j.com/appapi/region/{city_id}/v1/list'
urls_map={city['name']:base_url.format(city_id=city['city_id']) for city in citys}


class RegionDataTest(unittest.TestCase):

    @parameterized.expand([
        param(urls_map['北京'], {}),
        param(urls_map['杭州'], {}),

    ])
    def test_region_repeat(self,url,data):
        r = requests.post(url, data)
        res_data = r.json()['data']
        # res_data=test_data
        region_names= [i['name'] for i in res_data]
        is_repeat = assert_repeat(region_names)

        if is_repeat:
            logging.error('区域商圈 顶级区域重复，请人工检查!')
            # print('区域商圈 顶级区域重复，请人工检查!')

    @parameterized.expand([
        param(urls_map['北京'], {}),
        param(urls_map['杭州'], {}),

    ])
    def test_square_repeat(self,url,data):
        r = requests.post(url, data)
        res_data = r.json()['data']
        for i in res_data:
            region_name = i['name']
            square_name_data = i['sqlist']

            square_names = [j['name'] for j in square_name_data]
            is_repeat = assert_repeat( square_names)
            if is_repeat:
                logging.error('区域商圈 子区块重复! 请人工检查 %s区 二级区块！' % region_name)

if __name__ =='__main__':
    unittest.main(  )