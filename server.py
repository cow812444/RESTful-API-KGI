#/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2020年8月15日

@author: lishang chien

last edit: 2020年8月15日
'''
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from api import controller
import log

conf={}
conf['verbose'] = 'DEBUG'
conf['log_path'] = 'logs/'
log.setup_logging(conf)

#  Flask容器建立
api = Flask(__name__)
CORS(api)
set_ = Api(api)

#  route設置
controller.setup_route(set_)


if __name__ == "__main__":
    api.run(host= '0.0.0.0', port= 55688)