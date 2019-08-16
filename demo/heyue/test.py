#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:48:13 2018

@author: zhaobo
"""

from HuobiDMService import HuobiDM
from pprint import pprint

URL = "https://api.hbdm.com"

####  input your access_key and secret_key below:
ACCESS_KEY = "hrf5gdfghe-d9f5079e-c2cab0ea-b77dd"
SECRET_KEY = "a3e807f4-eec81c9e-9d0b1b73-5fa73"

dm = HuobiDM(URL, ACCESS_KEY, SECRET_KEY)

#### another account:
#dm2 = HuobiDM(URL, "ANOTHER ACCOUNT's ACCESS_KEY", "ANOTHER ACCOUNT's SECRET_KEY")


# print (u' 获取K线数据 ')
# pprint (dm.get_contract_kline(symbol='BTC_CW', period='60min', size=20))

print (u' 获取市场最近成交记录 ')
pprint (dm.get_contract_trade('BTC_CW',10))

# print (u' 批量获取最近的交易记录 ')
# pprint (dm.get_contract_batch_trade(symbol='BTC_CW', size=3))