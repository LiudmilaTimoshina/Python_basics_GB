#2 Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)

import re

LOG = 'nginx_logs.txt'

def log_parse(src):
    re_list = [r'\d{1,3}\.\d{1,3}\.\d{1.3}\.\d{1,3}',
               r'\[(.*?)\]',
               r'\"([A-Z]{3})',
               r'\s(\/[\w\/]+)',
               r'\s(\d{3})\s',
               r'\s\d{3}\s(\d+)']
    return tuple(re.findall(x,src)[0] for x in re_list)

if __name__ == '__main__':
    with open(LOG) as f:
        count, line = 1100, f.readline()
        while line and count:
            print(log_parse(line))
            count -= 1
            line = f.readline() 