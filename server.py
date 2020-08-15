#/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_restful_swagger_2 import Api
from flask_cors import CORS
from api import controller

'''
Created on 2020年8月15日

@author: lishang chien

last edit: 2020年8月15日
'''
#  Flask容器建立
api = Flask(__name__)
CORS(api)

#  swagger建置
set_ = Api(api,
    host='localhost:55688',
    schemes=['http'],
   # base_path='/dev',
    api_version='0.13',
    api_spec_url='/api/swagger',
    title='te-webhook3 API',
    description='IO & route  documents',
    contact={
        "name": "Emotibot",
        "url": "http://www.emotibot.com",
        "email": "lish4ang@gmail.com"
    },
    license={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
    }
)

#  route設置
controller.setup_route(set_)


if __name__ == "__main__":
    api.run(host= '0.0.0.0', port= 55688)