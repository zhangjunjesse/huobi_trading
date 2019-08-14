import requests
import json
import traceback



def get_kline(symbol="btcusdt",period="5min",size=200):
    r=requests.get('https://api.huobi.pro/market/history/kline?period='+period+'&size='+str(size)+'&symbol='+symbol)
    try:
        result = json.loads(r.text)
        if result['status'] == 'ok' :
            data = result['data']
            return data
    except:
        print("查询klin失败！")
        traceback.print_exc()
    return []

def get_depth(symbol="btcusdt",type="step2",depth=5):
    r=requests.get('https://api.huobi.pro/market/depth?symbol='+symbol+'&type='+type+'&depth='+str(depth))
    try:
        result = json.loads(r.text)
        if result['status'] == 'ok' :
            data = result['data']
            return data
    except:
        print("查询klin失败！")
        traceback.print_exc()
    return []

def get_market_trade(symbol="btcusdt"):
    r=requests.get('https://api.huobi.pro/market/trade?symbol='+symbol)
    try:
        result = json.loads(r.text)
        if result['status'] == 'ok' :
            data = result['data']
            return data
    except:
        print("查询klin失败！")
        traceback.print_exc()
    return []

def get_market_history_trade(symbol="btcusdt",size=200):
    r=requests.get('https://api.huobi.pro/market/history/trade?symbol='+symbol+'&size='+str(size))
    try:
        result = json.loads(r.text)
        if result['status'] == 'ok' :
            data = result['data']
            return data
    except:
        print("查询klin失败！")
        traceback.print_exc()
    return []


    
print(get_kline())
print(get_depth())
print(get_market_trade())
print(get_market_history_trade())