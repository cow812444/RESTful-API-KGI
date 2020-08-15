#/usr/bin/env python
# -*- coding: utf-8 -*-
from api import *

db_data = fake_db_data.db_data

def setup_route(api):

    api.add_resource(SqlDB, '/get/<db_name>/<key>/<value>')

    #api.add_resource(SqlDB, '/<string: db_name>/post/<string: key>/<string: value>')

    #api.add_resource(SqlDB, '/<string: db_name>/delete/<string: key>/<string: value>')

    #api.add_resource(SqlDB, '/<string: db_name>/put/<string: key>/<string: value>')


class SqlDB(Resource):
    def get(self, db_name, key, value):

        # 檢查db_name是否正確
        try: a = db_data[db_name]
        except Exception as e: raise e

        # 確認value是否存在key值中
        for customer_data in db_data[db_name]:
            if key in customer_data:
                if customer_data[key] == value:
                    return customer_data

        # 找不到key值或value不正確
        return {'message': 'key_error'}

    def post(self, db_name, key, value):
        pass

    def delete(self, db_name, key, value):
        pass

    def put(self, db_name, key, value):
        pass