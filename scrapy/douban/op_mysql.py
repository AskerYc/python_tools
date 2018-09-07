import pymysql
import json


def insertMany_top250(json_data):
    nrows = len(json_data)
    param = []
    for i in range(nrows):
        param.append([json_data[i]['serial_number'], json_data[i]['movie_name'], json_data[i]['actor'], json_data[i]['star'], json_data[i]['evaluate'], json_data[i]['describe']])
    try:
        sql = 'INSERT INTO douban_top250 values(%s, %s, %s, %s, %s, %s)'
        cursor.executemany(sql, param)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()


def get_json_data(path):
    f = open(path, 'rb+')
    load = json.load(f)
    return load


db = pymysql.connect('localhost', 'yucheng', 'yu10800258', 'crawled')
cursor = db.cursor()
insertMany_top250(get_json_data('./spiders/test.json'))

