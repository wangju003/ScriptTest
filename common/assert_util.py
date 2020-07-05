
def assert_repeat(data_list):
    '''
    判断指定列表中的元素是否数据重复
    :param region_name_list: 要判断的数据集合
    :return: is_repeat 重复True,不重复False
    '''
    count_element=set([data_list.count(x) for x in data_list])
    is_repeat=True if len(count_element)>1 else False
    return  is_repeat