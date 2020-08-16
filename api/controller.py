#/usr/bin/env python
# -*- coding: utf-8 -*-
from api import *

db_data = fake_db_data.db_data

def setup_route(api):

    # 查詢所有會員 : GET
    api.add_resource(Users, '/<db_name>')

    # 查詢 : GET , 刪除 : DELETE , 修改 : PUT
    api.add_resource(User, '/<db_name>/<pid>')

    # 新增會員 : POST
    api.add_resource(PostUser, '/<db_name>')

class Users(Resource):
    def get(self, db_name):
        if db_name not in db_data:
            return Response(json.dumps({'status':'404','message': 'Not Found'}), status=404)
        return Response(json.dumps(db_data[db_name]), status=200)


class User(Resource):
    def get(self, db_name, pid):

        # 檢查db_name是否正確
        if db_name not in db_data:
            return Response(json.dumps({'status':'404','message': 'Not Found'}), status=404)

        # 確認value是否存在key值中
        for customer_data in db_data[db_name]:
            if customer_data['PID'] == pid:
                return Response(json.dumps(customer_data), status=200)

        # 找不到key值或value不正確
        return Response(json.dumps({'status':'200','message': 'key_error'}), status=200)

    def delete(self, db_name, pid):
        pass

    def put(self, db_name, PID):
        pass

class PostUser(Resource):
    def post(self, db_name):
        json_from_request = jsonLoads(request.stream)
        required_args = []

        if db_name == 'cc':
            required_args = ['CampaignID', 'ProdType', 'CustName', 'MP1', 'MP2', 'O1', 'O2', 'H1', 'H2', 'H3', 'H4', '連絡人電話一', '戶籍1']
        elif db_name == 'gm':
            required_args = ['CampaignID', 'ProdType', 'CustName', 'MP1', 'MP2', 'O1', 'O2', 'H1', 'H2', 'H3', 'H4', '連絡人電話一', '戶籍1']
        else:
            return Response(json.dumps({'status':'404','message': 'Not Found'}), status=404)

        for args_ in required_args:
            if args_ not in json_from_request:
                return Response(json.dumps({'status':'400','message': 'Bad Request: '+args_}), status=400)

        db_data[db_name].append(json_from_request)
        return Response(json.dumps({'status':'201','message': 'Created'}), status=201)