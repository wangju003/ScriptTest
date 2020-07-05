

def generate_log():
    import logging, os
    dirname,filename = os.path.split(os.path.abspath(__file__))
    log_path = os.path.join(dirname, "assertLog.log")
    log_format = "[%(asctime)s][%(levelname)s] %(message)s"
    logging.basicConfig(format=log_format, filename=log_path, filemode="w", level=logging.DEBUG)
    console = logging.StreamHandler()
    console.setLevel(logging.ERROR)
    formatter = logging.Formatter(log_format)
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
    return logging
logging =generate_log()

#装饰器 参数化case中url的city_url
def param_city_url(base_url):
    from settings import citys
    city_ids = [city['city_id'] for city in citys]
    def deco(func):
        def wrapper(*args):
            for city_id in city_ids:
                url = base_url.format(city_id=city_id)
                func(*args, url)

        return wrapper
    return deco