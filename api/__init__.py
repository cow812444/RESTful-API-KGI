#/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Response
from flask import request
from flask_restful_swagger_2 import swagger, Resource

import sys
sys.path.append('..')
from db import fake_db_data