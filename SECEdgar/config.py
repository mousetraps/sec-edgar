# -*- coding:utf-8 -*-


import logging
import os

DEFAULT_DATA_PATH = os.environ.get('SEC_DATA_DIR') or os.path.abspath(os.path.join(
    os.path.dirname(os.getcwd()), 'SEC-Edgar-Data'))
