# -*- encoding: utf-8 -*-
"""
@File    : import_data.py
@Time    : 2019-6-10 上午 9:51
@Author  : major
@Email   : major3428@foxmail.com
@Software: PyCharm
"""

import pymongo
import funcy as fy

#pymongo
class MongodbConfig(object):
    #配置数据库
    host = 'localhost'
    port = 27017
    staff = 'staff'
    customer = 'customer'
    contact = 'contact'
    sales = 'sales'
    question = 'question'
    solution = 'solution'
    press = 'press'
    sourceid = 'sourceid'


    def __init__(self, database, collection, dict,host=None, port=None):
        self.host = host if host else self.host
        self.port = port if port else self.port
        self.database = database
        self.collection = collection
        self.dict = dict

    def _set_collection(self):
        """设置数据库"""
        client = pymongo.MongoClient(host=self.host, port=self.port)
        db = client[self.database]
        Collection = db[self.collection]

        return Collection

    def __load_dataframe(self):
        """读取dict"""
        # data = json.loads(j)
        data = self.dict
        return data

    def _combine_and_insert(self, data):
        """整合并插入数据"""
        # 构造 index 列表
        name_list = [self.staff, self.customer, self.contact, self.sales, self.question, self.solution,
                     self.press, self.sourceid]
        # 删除 None

        for i in range(len(name_list)):
            if None in name_list:
                name_list.remove(None)

        def process_data(n):
            # 返回单个数据的字典，key为index，若无index则返回 None
            single_data = {index.lower(): data.get(index, None) for index in name_list}

            return single_data

        lenth = len(data[self.press])  # 总长度
        coll = self._set_collection()

        # 插入数据

        for i in range(lenth):
            bar = process_data(i)
            coll.insert_one(bar)
            print('Inserting ' + str(i) + ', Total: ' + str(lenth))

    def __get_dups_id(self, data):
        """获得重复数据的id"""
        data['dups'].pop(0)

        return data['dups']

    def _drop_duplicates(self):
        """删除重复数据"""
        coll = self._set_collection()
        c = coll.aggregate([{"$group":
                                 {"_id": {'staff': '$staff'},
                                  "count": {'$sum': 1},
                                  "dups": {'$addToSet': '$_id'}}},
                            {'$match': {'count': {"$gt": 1}}}
                            ]
                           )
        data = [i for i in c]
        duplicates = fy.walk(self.__get_dups_id, data)
        dups_id_list = fy.cat(duplicates)

        for i in dups_id_list:
            coll.delete_one({'_id': i})
        # print("OK, duplicates droped! Done!")

    def data_to_db(self):
        """数据导入数据库"""
        data = self.__load_dataframe()
        self._combine_and_insert(data)
        self._drop_duplicates()
if __name__ == "__main__":
    # MGDB = MongodbConfig(database='zjnad',collection='customer')
    # MGDB.data_to_db()
    pass
